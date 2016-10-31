#!/usr/bin/python
#Filename : looptest.py

shoplist = ['apple','mango','carrot','banana']
shoplist.append('orange')
shoplist.sort()
print 'sholplist: ', shoplist
print 'indexing operation: ', shoplist[-1]
print 'slicing on a list: ', shoplist[2:-1]
del shoplist[0]
for i in shoplist:
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
