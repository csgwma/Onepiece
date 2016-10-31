# coding=utf-8
__author__ = 'Ace'

import sys


# 获取两个向量的内积（list表示向量）
def get_inner_product(list1, list2):
    if len(list1) != len(list2):
        sys.stderr('len(list1) != len(list2)')
        sys.exit(-1)
    _sum = 0.0
    for _i in range(len(list1)):
        _sum += list1[_i] * list2[_i]
    return _sum


# 获得向量的L2norm的平方
def get_l2_norm_sqaure(vec):
    _sum = 0.0
    for val in vec:
        _sum += val * val
    return _sum


# 获得向量的均值
def get_avg_val(vec):
    _sum = 0.0
    for val in vec:
        _sum += val
    return _sum / len(vec)


# 重置矩阵内的元素为0.0
def reset_matrix(m):
    for rix in range(len(m)):
        for cix in range(len(m[rix])):
            m[rix][cix] = 0.0
