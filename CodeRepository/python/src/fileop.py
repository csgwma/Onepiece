# coding=utf-8
__author__ = 'Ace'

# import pickle as p
import cPickle as p
import utilities

version = '0.1'

print 'utilities.maxval(5, 4)=',utilities.maxval(5, 4)

# 以下是正常的读写文件，推荐使用file()内建函数来创建文件对象
reader = open('input.txt', 'r')
writer = open('output.txt', 'w')
i = 0
for eachline in reader:
    # 注意下面输出 空行的影响 和 split()与split(' ')的区别
    print i, len(eachline), len(eachline.strip()), eachline.strip().split(), len(eachline.strip().split())  #注意空格的
    writer.write(str(i) + " " + eachline)  # 注意空行会有一个字符\n
    i += 1
# 另一种过时的写法
# while True:
#    line = reader.readline()
#    if len(line) == 0:
#        break
#    writer.write(str(i) + " " + line)  # 注意空行会有一个字符\n
#    i += 1

reader.close()
writer.close()

# 查看保存的文件对不对
reader = file('output.txt', 'r')
print 'file encoding =', reader.encoding
for eachline in reader:  # 文件也是可迭代的python数据类型
    print eachline,

print

reader.seek(0)  # 文件指针回到文件的开头
# 统计单词的个数
print '# word count =', len([word.strip() for line in reader for word in line.strip().split()])

reader.seek(0)  # 文件指针回到文件的开头
# 统计非空白字符的个数
print '# non-space char =', sum([len(word.strip()) for line in reader for word in line.strip().split()])
# 把中括号换为小括号或去掉，就是采用yield生成器表达式，节省内存
reader.seek(0)
print '# non-space char =', sum((len(word.strip()) for line in reader for word in line.strip().split()))

reader.seek(0)  # 文件指针回到文件的开头
# 找出文件最长的行的字符数
print 'max line size =', max(len(line.strip()) for line in reader)

# 任何python对象的存储
shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot', 'origne']

# 推荐如下file函数创建文件对象
f = file(shoplistfile, 'w')  # file() 内建函数是最近添加的，类似一个工厂函数，生成文件对象。如int()
p.dump(shoplist, f)  # dump the object to file
f.close()

del shoplist

f = file(shoplistfile, 'r')
storelist = p.load(f)

print storelist