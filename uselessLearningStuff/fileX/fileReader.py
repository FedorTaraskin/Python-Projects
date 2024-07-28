##https://youtu.be/XKHEtdqhLK8?si=KxmBQLKVT7YErFqK&t=10048
import os
from customModules import enclosingRemover

rawInput = input('Please paste a location here: ')
path = enclosingRemover.removeEnclosings(rawInput)
del (rawInput)

if os.path.exists(path): 
	if os.path.isfile(path):
		##Main code here
		with open (path) as file: print(file.read())
	elif os.path.isdir(path): print('That is a directory (folder).')
	else: print('It\'s not a file nor a directory, yet it exists?')
else: print ('Oops, no such thing! :(')