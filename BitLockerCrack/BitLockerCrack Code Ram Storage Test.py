import math
import os

attemptedCodes = []
def GenRecKey():
	global Rec_Key
	Rec_Key = ""
	for i in range(1,56):
		if i % 7 == 0:
			Rec_Key += "-"
		else:
			Rec_Key += str(math.floor((os.urandom(1)[0]/25.6)))
	return Rec_Key

while len(attemptedCodes) != 10**12:
	gendKey = GenRecKey()
	if gendKey not in attemptedCodes:
		attemptedCodes.append(GenRecKey())
		if len(attemptedCodes) == 10000:
			print(len(attemptedCodes))