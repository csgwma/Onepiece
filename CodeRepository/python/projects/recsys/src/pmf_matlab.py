# coding=utf-8
__author__ = 'Ace'
"""
这个代码是根据pmf作者提供的matlab源码更改，没有进行任何优化，跑起来很慢，迭代一次40s左右，比matlab慢多了
"""

import random
import mutilities
import math
import time

def initialized(trainfile, testfile, separator, start=0):
    """

    :param trainfile: 训练文件路径
    :param testfile: 测试文件路径
    :param separator: 分隔符
    :param start: 数据下标是从0还是从1开始
    :return:
    """
    train_vec = list()
    test_vec = list()
    for eachline in file(trainfile, 'r'):
        tokens = eachline.strip().split(separator)
        uid = int(tokens[0].strip()) - start
        mid = int(tokens[1].strip()) - start
        rating = float(tokens[2].strip())
        train_vec.append((uid, mid, rating))  # add a tuple(user_id, movie_id, rating)

    for eachline in file(testfile, 'r'):
        tokens = eachline.strip().split(separator)
        uid = int(tokens[0].strip()) - start
        mid = int(tokens[1].strip()) - start
        rating = float(tokens[2].strip())
        test_vec.append((uid, mid, rating))  # add a tuple(user_id, movie_id, rating)
    return train_vec, test_vec


# get the mean rating
def get_mean_rating(train_vec):
    sum = 0.0
    for vec in train_vec:
        sum += vec[2]
    return sum/len(train_vec)


# the test function for this modular
if __name__ == '__main__':
    trainfile = '../dataset/movietrain.csv'
    testfile = '../dataset/movietest.csv'
    separator = ','
    num_u = 6040
    num_m = 3952
    (train_vec, test_vec) = initialized(trainfile, testfile, separator, 1)

    pairs_tr = len(train_vec)
    pairs_te = len(test_vec)
    mean_rating = get_mean_rating(train_vec)
    print 'mean_rating = ', mean_rating
    epsilon = 500  # learning rate
    lambda_u = 0.01
    lambda_v = 0.01
    momentum = 0.8
    max_iteration = 100

    # 初始化数据
    num_feat = 10  # Rank 10 decomposition
    vecs_m = list()
    vecs_u = list()
    vecs_m_inc = list()
    vecs_u_inc = list()
    vecs_m_inc_new = list()
    vecs_u_inc_new = list()
    for i in range(num_u):
        row = list()
        row_zero = list()
        row_zero2 = list()
        for j in range(num_feat):
            row.append(random.random() * 0.1)
            row_zero.append(0.0)
            row_zero2.append(0.0)
        vecs_u.append(row)
        vecs_u_inc.append(row_zero)
        vecs_u_inc_new.append(row_zero2)

    for i in range(num_m):
        row = list()
        row_zero = list()
        row_zero2 = list()
        for j in range(num_feat):
            row.append(random.random() * 0.1)
            row_zero.append(0.0)
            row_zero2.append(0.0)
        vecs_m.append(row)
        vecs_m_inc.append(row_zero)
        vecs_m_inc_new.append(row_zero2)

    print 'begin iterate...'
    # 开始迭代求解
    for it in range(max_iteration):
        timestart = time.time()
        # random.shuffle(train_vec)  # 耗时 0.8s 但已经不需要了
        f_val = 0.0
        mutilities.reset_matrix(vecs_m_inc_new)
        mutilities.reset_matrix(vecs_u_inc_new)
        for apair in train_vec:
            pred_out = mutilities.get_inner_product(vecs_u[apair[0]], vecs_m[apair[1]])
            rating = apair[2] - mean_rating
            f_val += (pred_out - rating) ** 2
            f_val += 0.5 * lambda_u * mutilities.get_l2_norm_sqaure(vecs_u[apair[0]])
            f_val += 0.5 * lambda_v * mutilities.get_l2_norm_sqaure(vecs_m[apair[1]])
            for k in range(num_feat):
                vecs_m_inc_new[apair[1]][k] += 2 * (pred_out - rating) * vecs_u[apair[0]][k] + vecs_m[apair[1]][k] * lambda_v
                vecs_u_inc_new[apair[0]][k] += 2 * (pred_out - rating) * vecs_m[apair[1]][k] + vecs_u[apair[0]][k] * lambda_u

        # Update movie and user features
        for uid in range(len(vecs_u)):
            for k in range(num_feat):
                vecs_u_inc[uid][k] = vecs_u_inc[uid][k] * momentum + epsilon*vecs_u_inc_new[uid][k]/pairs_tr  # 这里的epsilon/pair_tr合为一个变量
                vecs_u[uid][k] -= vecs_u_inc[uid][k]

        for mid in range(len(vecs_m)):
            for k in range(num_feat):
                vecs_m_inc[mid][k] = vecs_m_inc[mid][k] * momentum + epsilon*vecs_m_inc_new[mid][k]/pairs_tr  # 进行修改
                vecs_m[mid][k] -= vecs_m_inc[mid][k]

        # Compute Predictions after Paramete Updates
        f_val = 0.0
        for apair in train_vec:
            pred_out = mutilities.get_inner_product(vecs_u[apair[0]], vecs_m[apair[1]])
            rating = apair[2] - mean_rating
            f_val += (pred_out - rating) ** 2
            f_val += 0.5 * lambda_u * mutilities.get_l2_norm_sqaure(vecs_u[apair[0]])
            f_val += 0.5 * lambda_v * mutilities.get_l2_norm_sqaure(vecs_m[apair[1]])
        err_train = math.sqrt(f_val/len(train_vec))

        # Compute predictions on the validation set
        f_val = 0.0
        for apair in test_vec:
            pred_out = mutilities.get_inner_product(vecs_u[apair[0]], vecs_m[apair[1]]) + mean_rating
            if pred_out > 5:
                pred_out = 5
            elif pred_out < 0:
                pred_out = 0
            rating = apair[2]  # 这里pred_out转换为原始值了，直接用apair[2]不用减去mean_rating了
            f_val += (pred_out - rating) ** 2
        err_test = math.sqrt(f_val/len(test_vec))

        timeconsumed = time.time() - timestart
        print 'time consumed : %3d,  iteration %3d   Train RMSE %6.4f,  Test RMSE %6.4f' % (timeconsumed, it, err_train, err_test)
    print 'run over'