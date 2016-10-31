# coding=utf-8
__author__ = 'Ace'
"""
这个代码是根据pmf作者提供的matlab源码更改，没有进行任何优化，跑起来很慢，迭代一次40s左右，比matlab慢多了

考虑 bias，但效果并不是那么好，是写的不对？
优化方向：
list 索引慢，换成字典dict

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


def get_bias(train_vec, mean_rating, num_u, num_m):
    bias_u = [0.0 for i in range(num_u)]
    bias_m = [0.0 for i in range(num_m)]
    cnt_u = [0 for i in range(num_u)]
    cnt_m = [0 for i in range(num_m)]
    for apair in train_vec:
        uid = apair[0]
        mid = apair[1]
        rating = apair[2]
        cnt_u[uid] += 1
        cnt_m[mid] += 1
        bias_u[uid] += (rating - mean_rating)
        bias_m[mid] += (rating - mean_rating)
    for i in range(num_u):
        if cnt_u[i] != 0 : bias_u[i] /= cnt_u[i]
    for i in range(num_m):
        if cnt_m[i] != 0 : bias_m[i] /= cnt_m[i]
    del cnt_u, cnt_m
    return bias_u, bias_m

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
    (bias_u, bias_m) = get_bias(train_vec, mean_rating, num_u, num_m)

    # hyper-parameters
    epsilon = 500  # learning rate
    lambda_u = 0.01
    lambda_v = 0.01
    lambda_bu = 0.001
    lambda_bv = 0.001
    momentum = 0.8
    max_iteration = 100

    # 初始化数据
    num_feat = 10  # Rank 10 decomposition
    vecs_m = [[random.random() * 0.1 for j in range(num_feat)] for i in range(num_m)]
    vecs_u = [[random.random() * 0.1 for j in range(num_feat)] for i in range(num_u)]
    vecs_m_inc = [[0.0 for j in range(num_feat)] for i in range(num_m)]  # 初始化一个num_m X num_feat 的0矩阵
    vecs_u_inc = [[0.0 for j in range(num_feat)] for i in range(num_u)]
    vecs_m_inc_new = [[0.0 for j in range(num_feat)] for i in range(num_m)]
    vecs_u_inc_new = [[0.0 for j in range(num_feat)] for i in range(num_u)]


    print 'begin iterate...'
    # 开始迭代求解
    for it in range(max_iteration):
        timestart = time.time()
        # random.shuffle(train_vec)  # 耗时 0.8s, 但已经不需要了
        f_val = 0.0
        mutilities.reset_matrix(vecs_m_inc_new)
        mutilities.reset_matrix(vecs_u_inc_new)
        for apair in train_vec:
            pred_out = mutilities.get_inner_product(vecs_u[apair[0]], vecs_m[apair[1]])
            rating = apair[2] - mean_rating - bias_u[apair[0]] - bias_m[apair[1]]
            f_val += (rating - pred_out) ** 2
            f_val += 0.5 * lambda_u * mutilities.get_l2_norm_sqaure(vecs_u[apair[0]])
            f_val += 0.5 * lambda_v * mutilities.get_l2_norm_sqaure(vecs_m[apair[1]])
            f_val += 0.5 * (lambda_bu * bias_u[apair[0]] + lambda_bv * bias_m[apair[1]])  # add bias term
            for k in range(num_feat):
                vecs_m_inc_new[apair[1]][k] += 2 * (rating - pred_out) * vecs_u[apair[0]][k] + vecs_m[apair[1]][k] * lambda_v
                vecs_u_inc_new[apair[0]][k] += 2 * (rating - pred_out) * vecs_m[apair[1]][k] + vecs_u[apair[0]][k] * lambda_u

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
            rating = apair[2] - mean_rating - bias_u[apair[0]] - bias_m[apair[1]]
            f_val += (pred_out - rating) ** 2
            f_val += 0.5 * lambda_u * mutilities.get_l2_norm_sqaure(vecs_u[apair[0]])
            f_val += 0.5 * lambda_v * mutilities.get_l2_norm_sqaure(vecs_m[apair[1]])
            f_val += 0.5 * (lambda_bu * bias_u[apair[0]] + lambda_bv * bias_m[apair[1]])  # add bias term
        err_train = math.sqrt(f_val/len(train_vec))

        # Compute predictions on the validation set
        f_val = 0.0
        for apair in test_vec:
            pred_out = mutilities.get_inner_product(vecs_u[apair[0]], vecs_m[apair[1]])
            pred_out += mean_rating + bias_u[apair[0]] + bias_m[apair[1]]
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