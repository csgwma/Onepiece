# coding=utf-8
__author__ = 'Ace'

import datetime


import math

writer = file('logtable.csv', 'w')
num = 20
for i in range(num):
    if i != num-1:
        writer.write(str(i+1) + ',')
    else:
        writer.write(str(i+1) + '\n')


for i in range(num):
    if i != num-1:
        writer.write(str(math.log(i+1, 2)) + ',')
    else:
        writer.write(str(math.log(i+1, 2)) + '\n')

writer.close()