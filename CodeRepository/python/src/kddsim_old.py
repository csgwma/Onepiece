# coding=utf-8
__author__ = 'Ace'

import math
import os

switch = [0,0,1,0,1,0,0,0,1,1]
entropy = [0,1,0,1,0,0,0,0,1,0]
lens = [1,1,1,0,1,1,1,1,0,1]
score = [1,0,1,0,1,0,1,1,0,1]
#debug = False
debug = True

# 计算两个向量的jaccard相似性(注意jaccard一般是判断两个集合的相似性的)
def sim_jaccard(vec1, vec2):
    sam_cnt = 0
    for i in range(len(vec1)):
        if vec1[i] == vec2[i]:
            sam_cnt += 1
    return float(sam_cnt) / (len(vec1) + len(vec2) - sam_cnt)


# 计算指标得分相比用户得分（groud truth）的accuracy。
def accuracy(vec1, vec2):
    sam_cnt = 0
    for i in range(len(vec1)):
        if vec1[i] == vec2[i]:
            sam_cnt += 1
    return float(sam_cnt) / 10



# 计算两个向量的consine相似性
def sim_cosine(vec1, vec2):
    total = 0.0
    size_1 = 0.0
    size_2 = 0.0
    for i in range(len(vec1)):
        total += vec1[i] * vec2[i]
        size_1 += vec1[i] ** 2
        size_2 += vec2[i] ** 2
    return total / (math.sqrt(size_1) * math.sqrt(size_2))


# 计算两个向量的Euclidean distance
def sim_euclidean(vec1, vec2):
    total = 0.0
    for i in range(len(vec1)):
        total += (vec1[i] - vec2[i]) ** 2
    return math.sqrt(total)


# 计算两个向量的 Manhattan  distance（在这个应用中都是0、1值，等于 Hamming distance）
def sim_manhattan(vec1, vec2):
    total = 0.0
    for i in range(len(vec1)):
        total += math.fabs(vec1[i] - vec2[i])
    return total


# 计算两个向量的 Hamming   distance（在这个应用中都是0、1值，等于Manhattan distance）
def sim_hamming(vec1, vec2):
    total = 0.0
    for i in range(len(vec1)):
        total += math.fabs(vec1[i] - vec2[i])
    return total


# 计算相似度，并返回平均相似度
def calc_sims_avg_new(datafile_pre, sim_fun, resultfile):
    results = list()
    # 读文件处理数据
    reader = file(datafile_pre)
    for eachline in reader:
        tokens = eachline.strip().split(',')
        vec3 = list()
        if debug:
            for val in tokens[0:6] + tokens[7:10]:
                vec3.append(int(val))
        else:
            for val in tokens:
                vec3.append(int(val))
        #  print vec3
        sims = list()
        if debug:
            # print 'switch[0:5]+switch[6:10]=',
            # print (switch[0:5]+switch[6:10])
            # print 'vec3 = ',
            # print vec3
            sims.append(sim_fun(switch[0:5]+switch[6:10], vec3))
            sims.append(sim_fun(entropy[0:5]+entropy[6:10], vec3))
            sims.append(sim_fun(lens[0:5] + lens[6:10], vec3))
            sims.append(sim_fun(score[0:5] + lens[6:10], vec3))
        else:
            sims.append(sim_fun(switch, vec3))
            sims.append(sim_fun(entropy, vec3))
            sims.append(sim_fun(lens, vec3))
            sims.append(sim_fun(score, vec3))

        results.append(sims)
    reader.close()

    total_switch = 0.0
    total_entropy = 0.0
    total_lens = 0.0
    total_score = 0.0
    writer = file(resultfile, 'w')
    writer.write('#%2s, %8s, %8s, %8s, %8s\n' % ('id', 'trans', 'entropy', 'lens', 'score'))
    id = 1
    for terms in results:
        writer.write('%3d, %.6f, %.6f, %.6f, %.6f\n' % (id, terms[0], terms[1], terms[2], terms[3]))
        total_switch += terms[0]
        total_entropy += terms[1]
        total_lens += terms[2]
        total_score += terms[3]
        id += 1
    # writer.write('\n')
    writer.close()
    size = len(results)
    return [total_switch/size, total_entropy/size, total_lens/size, total_score/size]


# 计算标准方差，并返回
def calc_sim_std(sim_fun, result_avg):
    sim_file = result_folder + sim_fun.func_name
    stds = [0.0, 0.0, 0.0, 0.0]
    cnt = 0
    for eachline in file(sim_file):
        if eachline.startswith('#'):
            continue
        cnt += 1
        tokens = list()
        for term in eachline.strip().split(','):
            tokens.append(float(term.strip()))
        tokens = tokens[1:]
        for i in [i for i in range(4)]:
            stds[i] += (tokens[i]-result_avg[i]) ** 2
    for i in range(len(stds)):
        stds[i] /= cnt
    return stds


# Z-test
def ztest(fun_list, results_avg, result_stds, cnt):
    zvals = dict()
    for fun_sim in fun_list:
        avg = results_avg[fun_sim.func_name]
        std = result_stds[fun_sim.func_name]
        zlist = list()
        s_ix = len(avg) - 1
        for i in range(len(avg)):
            zval = (avg[i] - avg[s_ix]) / math.sqrt(std[i]/cnt + std[s_ix]/cnt)
            zlist.append(math.fabs(zval))  # 取绝对值
        zvals[fun_sim.func_name] = zlist
    return zvals

# main function
if __name__ == '__main__':
    fun_list = [sim_jaccard, sim_cosine, sim_euclidean, sim_hamming, accuracy]
    # fun_list = [sim_cosine, sim_euclidean, sim_hamming]
    datafile = 'result106.csv'
    cnt = 106  # 记录总数
    result_folder = "../result/"
    results_avg = dict()
    for fun_sim in fun_list:
        avg = calc_sims_avg_new(datafile, fun_sim, result_folder + fun_sim.func_name)
        results_avg[fun_sim.func_name] = avg

    # 平均相似度 输出至文件
    wr = file(result_folder + os.sep + 'results_avg.csv', 'w')
    wr.write('#%12s, %8s, %8s, %8s, %8s\n' % ('sim_name', 'trans', 'entropy', 'lens', 'score'))
    # for key, avg in results_avg.items():  # 这样遍历不能保证有序
    for fun_sim in fun_list:
        avg = results_avg[fun_sim.func_name]
        wr.write('%13s, %.6f, %.6f, %.6f, %.6f\n' % (fun_sim.func_name, avg[0], avg[1], avg[2], avg[3]))
    wr.close()

    # 计算标准差 输出至文件
    result_stds = dict()
    for fun_sim in fun_list:
        std = calc_sim_std(fun_sim, results_avg[fun_sim.func_name])
        result_stds[fun_sim.func_name] = std
    wr = file(result_folder + os.sep + 'results_std.csv', 'w')
    wr.write('#%12s, %8s, %8s, %8s, %8s\n' % ('sim_name', 'trans', 'entropy', 'lens', 'score'))
    # for key, std in result_stds.items():  # 这样遍历不能保证有序
    for fun_sim in fun_list:
        std = result_stds[fun_sim.func_name]
        wr.write('%13s, %.6f, %.6f, %.6f, %.6f\n' % (fun_sim.func_name, std[0], std[1], std[2], std[3]))
    wr.close()

    # 计算Z-test， 输出至文件
    zvals = ztest(fun_list, results_avg, result_stds, cnt)
    wr = file(result_folder + os.sep + 'results_ztest.csv', 'w')
    wr.write('#%12s, %8s, %8s, %8s, %8s\n' % ('sim_name', 'trans', 'entropy', 'lens', 'score'))
    # for key, std in zvals.items():  # 这样遍历不能保证有序
    for fun_sim in fun_list:
        zval = zvals[fun_sim.func_name]
        wr.write('%13s, %.6f, %.6f, %.6f, %.6f\n' % (fun_sim.func_name, zval[0], zval[1], zval[2], zval[3]))
    wr.close()

    print 'run over'