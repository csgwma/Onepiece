# coding=utf-8
__author__ = 'Ace'


reader = file('iris.data.txt', 'r')
writer = file('iris.data.svm.txt', 'w')
formatstrp = '+1 1:%s 2:%s 3:%s 4:%s\n'
formatstrn = '-1 1:%s 2:%s 3:%s 4:%s\n'
for eachline in reader:
    tokens = eachline.strip().split(',')
    if len(tokens) != 5:
        print tokens
        continue
    if tokens[4] == 'Iris-setosa':
        writer.write(formatstrp % (tokens[0], tokens[1], tokens[2], tokens[3]))
    elif tokens[4] == 'Iris-versicolor':
        writer.write(formatstrn % (tokens[0], tokens[1], tokens[2], tokens[3]))
    else:
        pass
reader.close()
writer.close()


reader = file('wine.data.txt', 'r')
writer = file('wine.data.svm.txt', 'w')
formatstrp = '+1 1:%s 2:%s 3:%s 4:%s 5:%s 6:%s 7:%s 8:%s 9:%s 10:%s 11:%s 12:%s 13:%s\n'
formatstrn = '-1 1:%s 2:%s 3:%s 4:%s 5:%s 6:%s 7:%s 8:%s 9:%s 10:%s 11:%s 12:%s 13:%s\n'
for eachline in reader:
    tokens = eachline.strip().split(',')
    if len(tokens) != 14:
        print tokens
        continue
    if tokens[0] == '1':
        writer.write(formatstrp % (tokens[1], tokens[2], tokens[3], tokens[4], tokens[5], tokens[6], tokens[7], tokens[8], tokens[9], tokens[10], tokens[11], tokens[12], tokens[13]))
    elif tokens[0] == '2':
        writer.write(formatstrn % (tokens[1], tokens[2], tokens[3], tokens[4], tokens[5], tokens[6], tokens[7], tokens[8], tokens[9], tokens[10], tokens[11], tokens[12], tokens[13]))
    else:
        pass
reader.close()
writer.close()