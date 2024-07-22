import time
import random
text = "This should be animated"
chars = (("A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z"))
userinput = ""

while userinput != "exit":
	for i in text:
		print(str(chars[random.randint(0, 51)]), end="")
		time.sleep(0.04)
		print("\b", end="")
		time.sleep(0.04)
		print(i, end="")
		time.sleep(0.04)
	##userinput = input("\nType \"exit\" to exit.")
	print()
	time.sleep(1)
 
##Testing ground for line 7:
print(str(chr(random.randint(0, 127))), end="")
