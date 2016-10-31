# coding=utf-8
__author__ = 'Ace'

import os
import sys
import utilities
import fileop
from utilities import printdic

print '-'*25
print 'fileop.version = ', fileop.version
print 'utilities.version = ', utilities.version
print os.path.getsize('input.txt')

exec_code = compile('print [i*2 for i in range(5)]', '', 'exec')
exec exec_code

execfile('encoding.py')

# os.system('dir')


f = os.popen('dir')
i = 0
for line in f:
    print i, line,
    i += 1
f.close()

