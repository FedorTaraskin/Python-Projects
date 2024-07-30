##https://youtu.be/XKHEtdqhLK8?si=8vRl2mNfVlZGx6N_&t=10425
import os

src = r"D:\Fedor Taraskin\Desktop\pytest.txt"
dest = r"D:\pytestfolder\pytest.txt"
mode = input('Would you like to copy (c) or move (m) a file? (c/m): ')

if os.path.exists(src):
	if os.path.isfile(src):
		if mode == 'c': 
			from shutil import copy
			copy(src, dest)
			print(f'The file from {src} has been copied to {dest}.')
		elif mode == 'm':
			pass ##MOVING CODE HERE
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
else: print ('An unexpected ERROR ocurred, please send the developer a screenshot of this program.')