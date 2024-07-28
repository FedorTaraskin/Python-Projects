##https://youtu.be/XKHEtdqhLK8?si=RaLRZazKjOaWMY50&t=9820
import os

path = r'D:\Fedor Taraskin\Desktop'
rawInput = input('Please paste a location here: ')
enclosings = (("'", '"'))
for i in enclosings: rawInput = rawInput.removeprefix(i).removesuffix(i)
del(rawInput)

if os.path.exists(path): 
	print('ye, it exists', end=' ')
	if os.path.isfile(path): print('and it is a file')
	elif os.path.isdir(path): print('and it is a directory/folder')
	else: print('Hmm, it exists but it\'s not a file nor a directory?')
else: print ('oops, no such thing! :(')