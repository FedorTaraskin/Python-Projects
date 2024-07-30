##https://youtu.be/XKHEtdqhLK8?si=8vRl2mNfVlZGx6N_&t=10425
import os

def dirOrFile(path):
	if os.path.isfile(path): return 'file'
	elif os.path.isdir(path): return 'directory'
	else: raise ValueError

def overwriteConfirmation(path):
	pathType = dirOrFile(path)
	while os.path.exists(path):
		if input('The destination path exists. This will overwrite your {pathType}. If you do not wish to overwrite,\nrestart this program and select a different destination. Alternatively, you can move/delete the conflicting {pathType} Would you like to move your {dirorfolder} anyways? (Y/N): ').upper() == 'Y': break

src = r"D:\Fedor Taraskin\Desktop\pytest.txt"
dest = r"D:\pytestfolder\pytest.txt"
mode = input('Would you like to copy (c) or move (m) a file? (c/m): ')

if os.path.exists(src):
	overwriteConfirmation(dest)

	if os.path.isfile(src):
		if mode == 'c': 
			from shutil import copy
			copy(src, dest)
			print(f'The file from {src} has been copied to {dest}.')
		elif mode == 'm':
			os.replace(src, dest)
			print(f'The file from {src} has been moved to {dest}.')
			
	elif os.path.isdir(src):
		if mode == 'c':
			from shutil import copytree
			copytree(src, dest)
			print(f'The folder from {src} has been copied to {dest}.')
		elif mode == 'm':
			os.replace(src, dest)
			print(f'The folder from {src} has been moved to {dest}.')

	else: print('ERROR: The source path exists, but is not a file nor a directory.')
	
elif not os.path.exists(src): print ('Sorry, this path does not exist.')
else: print('An unexpected ERROR ocurred, please send the developer a screenshot of this program.')