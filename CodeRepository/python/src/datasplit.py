# coding=utf-8
__author__ = 'Ace'

import random

filename = 'iris.data.svm.txt'

incr1 = open(filename + '1.txt', 'w')
incr2 = open(filename + '2.txt', 'w')
incr3 = open(filename + '3.txt', 'w')
incr4 = open(filename + '4.txt', 'w')
incr5 = open(filename + '5.txt', 'w')


for eachline in file(filename):
    val = random.random()
    if val < 0.2:
        incr1.write(eachline)
    elif val < 0.4:
        incr2.write(eachline)
    elif val < 0.6:
        incr3.write(eachline)
    elif val < 0.8:
        incr4.write(eachline)
    elif val < 1.0:
        incr5.write(eachline)
    else:
        pass
incr1.close()
incr2.close()
incr3.close()
incr4.close()
incr5.close()
