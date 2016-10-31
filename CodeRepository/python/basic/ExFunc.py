# encoding = utf-8
# Filename: ExFunc.py
# Date: Thu Jul 17 15:24:46 CST 2014


# print the message n times
def print_msg(msg, times=1):
    print msg*times


print_msg("hello!", 3)


def max(a, b=0, c= -1):
    """Print the maximum of two or three positive numbers.
    The two or three values must be integers."""  # there signal quotes. Docstring
    b = int(b)
    c = int(c)
    a = int(a)

    if a > b:
        return a
    else:
        return b

if __name__ == '__main__':
    a = 3
    b = 4
    
    print('a= ', a, ', b=', b)
    print('The big num. is ', max(a, b))
    
    print max(c=5, b=3, a=10)  # use the key parameters, indicate the para name without caring the order
    print max.__doc__

