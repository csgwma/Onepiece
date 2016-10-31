# coding=utf-8
__author__ = 'Ace'

import nltk
import time

sentence = '''At eight o'clock on Turesday morning Arthor didn't feel ver good.'''

timebeg = time.time()
print timebeg

i = 0
while i < 100:
	nltk.word_tokenize(sentence)
	i += 1

timeend = time.time()

print timeend
print timeend - timebeg


# slice切片操作
shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist.append('orange')
shoplist.sort()
print 'shoplist: ', shoplist
print 'indexing operation: ', shoplist[-1]
print 'slicing on a list: ', shoplist[2:-1]
del shoplist[0]  # python从 0 开始计数
for i in range(1, 7, 2):
	print i
else:
	print("the for loop is over!")

num = 23
flag = True
while flag:
	guess = int(raw_input("enter a guess number:"))
	if guess == num:
		print('you guessed it! Con~')
		break
	elif guess < num:
		print('larger than your guessed number')
		continue
		print("this line will not be displayed!")
	else:
		print('less than your guessed number')
else:
	print('The while loop is over')

print 'Done'

