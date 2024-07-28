##https://youtu.be/XKHEtdqhLK8?si=KxmBQLKVT7YErFqK&t=10048
import os

path = input('Please paste a location here: ')
enclosings = (("'", '"'))
for i in enclosings: path = path.removeprefix(i).removesuffix(i)

if os.path.exists(path): 
	if os.path.isfile(path):
		##Main code here
		with open (path) as file: print(file.read())
	elif os.path.isdir(path): print('That is a directory (folder).')
	else: print('It\'s not a file nor a directory, yet it exists?')
else: print ('Oops, no such thing! :(')