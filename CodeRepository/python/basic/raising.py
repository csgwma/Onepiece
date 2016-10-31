#!/usr/bin/python
# Filename: raising.py

import sys


class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    s = raw_input('Enter something --> ')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
    # Other work can continue as usual here
except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException, x:
    print 'ShortInputException: The input was of length %d, \
was expecting at least %d' % (x.length, x.atleast)

else:  # try语句块，运行完，没有发生异常才会执行此语句块
    print 'No exception was raised.'

finally:  # 无论try语句块是否发生异常，都执行finally语句块,
    print
    # finally 会自动的重新引发异常