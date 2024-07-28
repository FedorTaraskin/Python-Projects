def removeEnclosings(text):
	enclosings = (("'", '"'))
	for i in enclosings: text = text.removeprefix(i).removesuffix(i)
	return text