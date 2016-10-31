# coding=utf-8
# "This is the document of this module
__author__ = 'Ace'

version = '0.1'

print 'load module:  utilities.py', 'version = ',version


def reverse(x):
    """
    DocStrings: return the reverse of an interger

    :param x:
    :return: reverse x
    """
    s = ''
    ix = 0
    x = str(x)
    if x[0] == '-':
        s += x[0]
        ix = 1
    beg = len(x) - 1
    while x[beg] == '0' and beg > 0:
        beg -= 1

    if ix == 0:
        s += x[beg::-1]
    else:
        s += x[beg:0:-1]
    return s


def maxval(x, y):
    if x > y:
        return x
    else:
        return y
maxval.version = '0.1'  #该函数添加属性
maxval.__doc__ = 'return the bigger value in (x,y)' #该函数添加属性


def sumlist(initval=0, *args):
    """
    return the sum of the values in list args
    :param initval:
    :param args:
    :return:
    """
    total = initval
    for i in args:
        total += i
    return total


def foo(val):
    x = 0
    x += val
    def foo2():
        print 'hello foo2()'

    return x


# print the key-value in dictionary
def printdic(**dics):
    x = 6
    for key, val in dics:
        print "%s : %s" % (key, val)


# the test codes for the functions in the module
if __name__ == '__main__':

    # test function
    def test():
        print maxval(1, 3)
        print max(0, range(5))

    # test()