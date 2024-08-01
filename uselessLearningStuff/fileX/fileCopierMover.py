##https://youtu.be/XKHEtdqhLK8?si=8vRl2mNfVlZGx6N_&t=10425
import os

src = r"D:\Fedor Taraskin\Desktop\TASAS ADVAS 1BACH.pdf"
dest = r"D:\Inside of this folder is the pytestfolder"
if os.path.isdir(src): dest = dest + src[src.rfind('\\'):]
mode = input('Would you like to copy (c) or move (m) a file? (c/m): ').lower()

def dirOrFile(path):
	if os.path.isfile(path): return 'file'
	elif os.path.isdir(path): return 'directory'

def overwriteConfirmation(path):
	pathType = dirOrFile(path)
	while os.path.exists(path):
		if input(f'The destination path exists. This will overwrite your {pathType}. If you do not wish to overwrite,\nrestart this program and select a different destination. Alternatively, you can move/delete the conflicting {pathType} Would you like to move your {pathType} anyways? (Y/N): ').upper() == 'Y': break

def main():
	if os.path.exists(src):
		if overwriteConfirmation(dest) == None: os.makedirs(dest)
		if os.path.isfile(src):
			if mode == 'c': 
				from shutil import copy
				copy(src, dest)
				print(f'The file from\n{src}\nhas been copied to\n{dest}.')
				
		elif os.path.isdir(src):
			if mode == 'c':
				from shutil import copytree
				copytree(src, dest)
				print(f'The folder from\n{src}\nhas been copied to\n{dest}.')

		else: print('ERROR: The source path exists, but is not a file nor a directory.')

		##This bit of code has been moved out of [elif os.path.is[dir/file](src):] because os.replace works for files and DIRs.
		##shutil.copy() only works for files, and copytree() for DIRs.
		if mode == 'm':
				os.replace(src, dest) ##HOW COME I AM GETTING PERMISSION ERROR?!
				print(f'The file from\n{src}\nhas been moved to\n{dest}.')

	elif not os.path.exists(src): print('The destination path does not exist.')
	else: print('An unexpected ERROR ocurred, please send the developer a screenshot of this program.\nThe src path exists but also doesn\'t at the same time.')

main()