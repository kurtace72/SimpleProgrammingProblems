#!/usr/bin/python3.6

import random

#1
#print('Hello World')

#2
#name = input('Please insert your name>')
#print('Hello ' + name)

#3
#name = input('Please insert your name>')
#if name == 'Alice':
#	print('Hello ' + name)
#elif name == 'Bob':
#	print('Hello ' + name)
#else:
#	pass

#4
#number = input('Please insert a number> ')
#print(sum(range(1,int(number)+1)))

#5
#number = input('Please insert a number> ')
#total = 0
#for i in range(1,int(number)+1):
#	if i%3==0:
#		total += i
#	elif i%5==0:
#		total += i
#	else:
#		pass
#print(total)

#6
#def product(n):
#	return 
#number = input('Please insert a number> ')
#choice = input('Would you like to:\n1: Sum up the numbers\n2: Calculate the'
#				'product.\nPlease insert the number of your choice> ')
#if choice == '1':
#	print(sum(range(1,int(number)+1)))
#elif choice == '2':
#	total = 1
#	for i in range(1, int(number)+1):
#		total *= i
#	print(total)
#else:
#	print('Not a valid choice. Exiting..')

#7
#for i in range(1,13):
#	print('Multiplication table for the number: ', i)
#	for num in range(1,11):
#		print(num, '*', i, '=',  i*num)
#	print('\n')

#8
#for i in range(1,101):
#	prime = True
#	for num in range(2,i):
#		if i%num == 0:
#			prime = False
#	if prime:
#		print(i)

#9
print('Guess the number!')
number = random.randint(1,100)
done = False
