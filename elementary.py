#!/data/data/com.termux/files/usr/bin/python3.6

import random, datetime, calendar

def main():
	running = True
	print('There are eleven exercises. After you have choosen one '
			'you will be promted with a text telling you what will '
			'happen.\n')
	while running:
		try:
			choice = input('Please insert the number of exercise you want to '
							'execute or "exit" to leave. > ')
			if choice == '1':
				one()
			elif choice == '2':
				two()
			elif choice == '3':
				three()
			elif choice == '4':
				four()
			elif choice == '5':
				five()
			elif choice == '6':
				six()
			elif choice == '7':
				seven()
			elif choice == '8':
				eight()
			elif choice == '9':
				nine()
			elif choice == '10':
				ten()
			elif choice == '11':
				eleven()
			elif choice == 'exit':
				running = False
			else:
				print('Not a valid choice. Exiting..')

			print('Your last choice was: ' + choice)
		except EOFError:
			running = False

#1
def one():
	print('Printing "Hello World".')
	print('Hello World')
	print(' ')

#2
def two():
	print('Greeting the user by name.')
	name = input('Please insert your name>')
	print('Hello ' + name)
	print(' ')

#3
def three():
	print('Only greet users named "Alice" and "Bob".')
	name = input('Please insert your name>')
	if name == 'Alice':
		print('Hello ' + name)
	elif name == 'Bob':
		print('Hello ' + name)
	else:
		pass
	print(' ')

#4
def four():
	print('Sum up the numbers 1..n.')
	number = input('Please insert a number> ')
	print(sum(range(1,int(number)+1)))
	print(' ')

#5
def five():
	print('Sum up only prime numbers 1..n.')
	number = input('Please insert a number> ')
	total = 0
	for i in range(1,int(number)+1):
		if i%3==0:
			total += i
		elif i%5==0:
			total += i
		else:
			pass
	print(total)
	print(' ')

#6
def six():
	print('Sum up 1..n or return the product 1..n.')
	def product(n):
		return 
	number = input('Please insert a number> ')
	choice = input('Would you like to:\n1: Sum up the numbers\n2: Calculate the'
					'product.\nPlease insert the number of your choice> ')
	if choice == '1':
		print(sum(range(1,int(number)+1)))
	elif choice == '2':
		total = 1
		for i in range(1, int(number)+1):
			total *= i
		print(total)
	else:
		print('Not a valid choice. Exiting..')
	print(' ')

#7
def seven():
	print('Print multiplication tables 1..12.')
	for i in range(1,13):
		print('Multiplication table for the number: ', i)
		for num in range(1,11):
			print(num, '*', i, '=',  i*num)
		print('\n')
	print(' ')
	
#8
def eight():
	print('Print all prime numbers in range 1..100.')
	for i in range(1,101):
		prime = True
		for num in range(2,i):
			if i%num == 0:
				prime = False
		if prime:
			print(i)
	print(' ')

#9
def nine():
	print('The user has to guess the number.')
	print('Guess the number!')
	number = random.randint(1,10)
	running = True
	tries = []
	while running:
		guess = input('Please insert a number between 1 and 10 > ')
		try:
			value = int(guess)
		except ValueError:
			print('That is not an integer. Exiting..')
			running = False
		if value not in tries:
			tries.append(value)
		if value == number:
			print('Yeah that\'s right!')
			running = False
		else:
			if value < number:
				print('My number is bigger. Try again.\n')
			else:
				print('My number is smaler. Try again.\n')

	print('Number of tries needed: ', len(tries))
	print(' ')

#10
def ten():
	print('Print next 20 leap years from now.')
	counter = 0
	year = datetime.datetime.now().year
	while counter < 20:
		if calendar.isleap(year):
			counter += 1
			print('%s is leap year' % (year))
		year += 1 

	print(' ')

#11
def eleven():
	print('Calculation of pi.')
	result = 0
	x = 1
	while x < 10**6:
		result += ((-1)**(x+1))/(2*x-1)
		x += 1
	result *= 4
	print(result)
	print(' ')

#typical boilerplate to start if module is not imported
if __name__ == "__main__":
	main()
