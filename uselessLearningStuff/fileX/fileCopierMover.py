##https://youtu.be/XKHEtdqhLK8?si=8vRl2mNfVlZGx6N_&t=10425
from os import path

src = r"D:\Fedor Taraskin\Desktop\pytestfolder\TASAS ADVAS 1BACH.pdf"
dest = r"D:\Inside of this folder is the pytestfolder"
if path.isdir(src): dest = dest + src[src.rfind('\\'):]
mode = None
while not (mode == 'c' or mode == 'm'): mode = input('Would you like to copy (c) or move (m) a file? (c/m): ').lower()

def dirOrFile(pathArg):
	if path.isfile(pathArg): return 'file'
	elif path.isdir(pathArg): return 'directory'

def overwriteConfirmation(pathArg):
	pathType = dirOrFile(pathArg)
	while path.exists(pathArg):
		if input(f'The destination path exists. This will overwrite your {pathType}. If you do not wish to overwrite,\nrestart this program and select a different destination. Alternatively, you can move/delete the conflicting {pathType} Would you like to move your {pathType} anyways? (Y/N): ').upper() == 'Y': break
	
	if path.exists(pathArg):
		if path.isdir(pathArg): 
			from shutil import rmtree
			rmtree(pathArg)
		elif path.isfile(pathArg):
			from os import remove
			remove(pathArg)

def main():
	if path.exists(src):
		overwriteConfirmation(dest)
		if not path.exists(dest): 
			from os import makedirs
			makedirs(dest)

		if mode == 'c':
			if path.isfile(src):
				from shutil import copy2
				copy2(src, dest)
				print(f'The file from\n{src}\nhas been copied to\n{dest}.')

			elif path.isdir(src):
				from shutil import copytree
				copytree(src, dest)
				print(f'The folder from\n{src}\nhas been copied to\n{dest}.')

			else: print('ERROR: The source path exists, but is not a file nor a directory.\nPlease send the developer a screenshot of this program.')

		elif mode == 'm':
				from shutil import move
				move(src, dest) ##HOW COME I AM GETTING PERMISSION ERROR?!
				print(f'The file from\n{src}\nhas been moved to\n{dest}.')

	elif not path.exists(src): print('The source path does not exist.')
	else: print('An unexpected ERROR ocurred, please send the developer a screenshot of this program.\nThe src path exists but also doesn\'t at the same time.')

main()