#!/usr/bin/env python

from random import randrange as rr

def randGen(aList):
    while aList:
	yield aList.pop(rr(len(aList)))


def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1

if __name__ == '__main__':
    for item in randGen(['rock', 'paper', 'scissors']):
	print item

    count = counter(5)
    print count
    print count.next()
    print count.next()
    print count.send(9)
    print count.next()
    print count.close()
