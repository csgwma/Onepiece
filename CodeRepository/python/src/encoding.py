# coding=utf-8
__author__ = 'Ace'

import sys

# 返回当前系统所使用的默认字符编码
print sys.getdefaultencoding()  # 输出 ascii
# 返回用于转换Unicode文件名至系统文件名所使用的编码
print sys.getfilesystemencoding()  # 输出 mbcs


s1 = '马国hi'
s1u = u'马国hi'
print "s1=", s1, '  len(s1)=', len(s1)
print "s1u=", s1u, '  len(s1u)=', len(s1u)

# for s in s1:
#    print s

s2 = "maguoe"  # s2 必须是ascii字符，才可以正确decode
print s2.decode("ascii").encode("utf-8")

