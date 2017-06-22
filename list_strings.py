#!/data/data/com.termux/files/usr/bin/python

def main():
	#test values
	list1 = [1,2,3,4,5,3,5,7,8,2]
	list2 = [1,2,3,4,5,3,5,7,8,2]
	integer = 12
	string = 'ala'
	running = True
	while running:
		try:
			choice = input('Please choose a exercise to execute or type "exit"'
					' to leave > ')
			if choice == '1':
				one(list1)
			elif choice == '2':
				two(list1)
			elif choice == '3':
				three(list1, integer)
			elif choice == '4':
				four(list1)
			elif choice == '5':
				five(list1)
			elif choice == '6':
				six(string)
			elif choice == '7':
				seven(list1)
			elif choice == '8':
				on_all(multi, list1)
			elif choice == '9':
				nine(list1, list2)
			elif choice == '10':
				ten()
			elif choice == '11':
				eleven()
			elif choice == '12':
				twelve()
			elif choice == '13':
				thirteen()
			elif choice == '14':
				fourteen()
			elif choice == '15':
				fivteen()
			elif choice == '16':
				sixteen()
			elif choice == '17':
				seventeen()
			elif choice == '18':
				eightteen()
			elif choice == '19':
				nineteen()
			elif choice == '20':
				twenty()
			elif choice == 'exit':
				running = False
			else:
				print('Not a valid choice. Exiting..')
		except EOFError:
			running = False

# for 8
def multi(n):
	return n*n
#1
def one(elements):
	print('Print the biggest value in a given list.')
	biggest = 0
	for elm in elements:
		try:
			value = int(elm)
		except ValueError:
			print('The list must contain only integers.')
		if value > biggest:
			biggest = value
	print('The biggest value is: ', biggest)
	print(' ')

#2
def two(elements):
	print('Reverse a list in place.')
	print('Original list: ', elements)
	print('Reversed list: ', elements[::-1])

#3 
def three(elements, elm):
	print('Tell us if element is in list.')
	if elm in elements:
		print('Yes.')
	else:
		print('No.')
	print(' ')

#4
def four(elements):
	print('Only print elements on odd positions.')
	for elm in elements:
		if not elements.index(elm)%2  == 0:
			print(elm)	
	print(' ')

#5
def five(elements):
	print('Compute the running total.')
	print(sum(elements))
	print(' ')

#6
def six(string):
	print('Check if a string is a palindrome.')
	if string == string[::-1]:
		print('It is.')
	print(' ')

#7
def seven(elements):
	print('Calculate the running total bu for loop, while lop and recursion.')
	def foorloop(elements):
		total = 0
		for elm in elements:
			total += elm
		print(total)
	def whileloop(elements):
		total = 0
		counter = 0
		while counter < len(elements):
			total += elements[counter]
			counter += 1
		print(total)
	def recursion(elements):
		if len(elements) == 1:
			return elements[0]
		return elements[0] + recursion(elements[1:])

	foorloop(elements)
	whileloop(elements)
	print(recursion(elements))
	print(' ')

#8
def on_all(function, elements):
	print('Apply a function to every element of a list.')
	result =  map(function, elements)
	print(set(result))
	print(' ')

#9
def nine(list1, list2):
	print('Concatenate two lists.')
	print(list1 + list2)
	print(' ')



if __name__ == "__main__":
	main()








