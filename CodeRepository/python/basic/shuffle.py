#!/usr/bin/python
#Filename: shuffle.py
import random

filename = "filename"

filename_new = filename + "_new"

lines = list()
line_num = 0
for line in open(filename):
    lines.append(line)    # 这里没有判断是不是空行
    line_num += 1

indexes = range(line_num)
random.shuffle(indexes)
writer = open(filename_new, 'w')
for ix in indexes:
    writer.write(lines[ix])

writer.close()