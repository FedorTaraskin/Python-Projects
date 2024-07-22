stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 2, 'arrow': 12, 'baby': 999}

def displayInventory(inventory):
	print("Inventory:")
	for i,v in inventory.items():
		##Multiple if statements that check the item's
		##last letters, and fixes the plural word
		if v == 1:
			print(v, i)
		elif v > 1 and (i[-1:] == "s" or i[-2:] == "sh" or i[-2:] == "ch" or i[-1:] == "x" or i[-1:] == "z"):
			print(v, i + "es")
		elif i[-1:] == "y":
			print(v, i + "\bies")
		else:
			print(v, i + "s")
		totalItems = 0
	for i in inventory:
		totalItems += inventory[i]
	print("\nTotal number of items: " + str(totalItems))

#displayInventory(stuff)

def addToInventory(inventory, addedItems):
	for item in addedItems:
		if item in inventory:
			inventory[item] += 1
		else:
			inventory[item] = 1
	return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = (('gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'))
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)