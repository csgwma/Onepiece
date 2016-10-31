# coding=utf-8
__author__ = 'Ace'


def add(x, y):
    return x + y


sum = 0
for i in range(1,11):
    sum = add(sum, i)

print sum