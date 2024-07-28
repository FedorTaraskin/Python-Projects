def removeenclosings(rawInput):
	enclosings = (("'", '"'))
	for i in enclosings: rawInput = rawInput.removeprefix(i).removesuffix(i)
	path = rawInput
	del(rawInput)