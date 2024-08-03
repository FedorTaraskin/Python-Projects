from time import sleep
from random import randint
text = "This should be animated"
chars = (("A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"))
userinput = ""

while userinput != "exit":
	for i in text:
		print(str(chars[randint(0, 51)]), end="")
		sleep(0.04)
		print("\b", end="")
		sleep(0.04)
		print(i, end="")
		sleep(0.04)
	##userinput = input("\nType \"exit\" to exit.")
	print()
	sleep(1)
 
##Testing ground for line 7:
print(str(chr(randint(0, 127))), end="")
