# !/usr/bin/python
# Filenname reverseInt.py


def reverse(x):
    s = ''
    ix = 0 
    x = str(x)
    if x[0] == '-':
        s += x[0]
        ix = 1
    beg = len(x)-1
    while (x[beg] == '0' and beg > 0):
        beg -= 1
    
    if ix == 0:
        s += x[beg::-1]
    else: 
        s += x[beg:0:-1]    
    return s
    
print (reverse(-34500))
print (reverse(34500))
print (reverse(3))
print (reverse(0))
print (reverse(-0))
print (reverse(-5))
print (reverse(-0))
print ('over')
