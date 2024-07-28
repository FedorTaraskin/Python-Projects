x = 0

def theFunc():
	global x
	x += 1
	print(x)
	theFunc()

theFunc()