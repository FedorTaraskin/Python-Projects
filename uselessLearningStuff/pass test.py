'''
def printAllBut3():
	for i in range(10):
		if i == 3:
			pass
		else:
			print(i)

##https://chatgpt.com/share/2444f177-f557-40af-bb70-cea0c0f2a627

def practice(input):
	try:
		input = int(input)
	except ValueError:
		print('I said DECIMAL.')
	match input:
		case 0:
			print("Issa zero.")
		case _ if input > 0:
			print('It\'s positive.')
		case _ if input < 0:
			##Use one of the two, these are the options
			pass
			raise NotImplementedError
'''
		
def practice2(input):
	if type(input) != list:
		raise ValueError
	##Checks for dupes, and merges them.
	for tuple in input: ##each tuple in the list
		for a in input: ##I need to get some sleep ---------------
			if a[0] == tuple[0]:
				#tuple[1] += a[1]
				print(tuple[1])
				input.remove(a)

practice2List = [('apple', 3), ('kiwi', 9), ('orange', 4), ('apple', 1), ('banana', 7279), ('orange', 14)]

for i in range (5):
	#practice(input('Gimme a decimal number: '))
	practice2(practice2List)