##https://youtu.be/XKHEtdqhLK8?si=8vRl2mNfVlZGx6N_&t=10425
from shutil import copy

src = r"D:\Fedor Taraskin\Desktop\pytest.txt"
dest = r"D:"
mode = input('Would you like to copy (c) or move (m) a file? (c/m): ')
if mode == 'c': copy(src, dest)
elif mode == 'm':
	import os
	
else: 'Incorrect mode selection. Please try again and input either "c" or "m".'