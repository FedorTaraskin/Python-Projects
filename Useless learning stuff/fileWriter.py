##https://youtu.be/XKHEtdqhLK8?si=zKHhk2tvsr6zMERP&t=10260
import os

enclosings = (("'", '"'))
rawInput = input('Please paste a location here: ')
for i in enclosings: rawInput = rawInput.removeprefix(i).removesuffix(i)
path = rawInput
del(rawInput)

if os.path.exists(path): 
	if os.path.isfile(path):
		with open (path) as fileToBuffer: fileBuffer = fileToBuffer.read()
		modeChoice = input('Would you like to overwrite (w) the file or append to (a) the file? w/a: ')
		if modeChoice == 'w': 
				inputBuffer = input('What would you like to write?\nYou can use ' + r'"\n"' + ' to make a new line: ')
				with open (path, 'w') as file: file.write(inputBuffer.replace(r'\n', '\n'))
				del(inputBuffer)
		elif modeChoice == 'a': 
				##The inputBuffer is to give the user the ability to make new lines (by typing \n), as pressing enter will submit the text.
				inputBuffer = input('What would you like to append?\nYou can use' + r'"\n"' + 'to make a new line: ')
				with open (path, 'a') as file: file.write(inputBuffer.replace(r'\n', '\n'))
				del(inputBuffer)
		else: 
				print('Incorrect choice. You can only select between "w" and "a".')
				exit()
			
		with open (path) as file: print(f'This is what the file looked like before your changes: {fileBuffer}\nand this is what the file looks like after your changes: {file.read()}')
		
	elif os.path.isdir(path): print('That is a directory (folder). Please select a file and not a directory.')
	else: print('It\'s not a file nor a directory, yet it exists? Please send a screenshot to the developer of this program.')
else: print ('Oops, no such thing! :(')