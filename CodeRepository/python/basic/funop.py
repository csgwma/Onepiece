# coding=utf-8
# 练习内容:
# 1. 将一个函数作为形参传递

__author__ = 'Ace'


def sum_list(seq):
    total = 0
    for val in seq:
        total += val
    return total


def multiply_list(seq):
    total = 1
    for val in seq:
        total *= val
    return total


# 将一个函数作为形参传递
def fun_list(fun, seq):
    return fun(seq)


if __name__ == '__main__':
    seq = [i+1 for i in range(5)]
    print fun_list(sum_list, seq)  # 15
    print fun_list(multiply_list, seq)  # 120