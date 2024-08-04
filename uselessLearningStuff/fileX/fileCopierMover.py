##https://youtu.be/XKHEtdqhLK8?si=8vRl2mNfVlZGx6N_&t=10425
from os import path
print('Note: folders are also named directories ocasionally.')

src = input('Please input the file/folder you want to copy or move: ')
dest = input('Please input the destination for your file: ')
if path.isdir(src): dest += src[src.rfind('\\'):] ##if the source is a directory, add it to the destination (so that it doesn't overwrite the dest dir)
mode = None

def dirOrFile(pathArg):
	if path.isfile(pathArg): return 'file'
	elif path.isdir(pathArg): return 'directory'

while not (mode == 'c' or mode == 'm'): mode = input(f'Would you like to copy (c) or move (m) the {dirOrFile(src)}? (c/m): ').lower()

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
				move(src, dest)
				print(f'The file from\n{src}\nhas been moved to\n{dest}.')

	elif not path.exists(src): print('The source path does not exist.') ##TODO/ERROR: Sometimes this triggers wrongly. Ex: src = "D:\Fedor Taraskin\Desktop\pytestfolder"
	else: print('An unexpected ERROR ocurred, please send the developer a screenshot of this program.\nThe src path exists but also doesn\'t at the same time.')

main()