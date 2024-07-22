guestDictionary = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for guestName, guestsItem in guests.items(): ##Remember that dictionary.items() returns both the key and the value
        ##print(k,v)
        numBrought += guestsItem.get(item, 0)
    return numBrought

def hardcodedPrints():
    print('Number of things being brought:')
    print(' - Apples.........' + str(totalBrought(guestDictionary, 'apples')))
    print(' - Cups...........' + str(totalBrought(guestDictionary, 'cups')))
    print(' - Cakes..........' + str(totalBrought(guestDictionary, 'cakes')))
    print(' - Ham Sandwiches.' + str(totalBrought(guestDictionary, 'ham sandwiches')))
    print(' - Apple Pies.....' + str(totalBrought(guestDictionary, 'apple pies')))
hardcodedPrints()

'''def automated():
    print("\nNow for an automated run... possibly.")
    for guestName,guestsItem in guestDictionary.items():
        ##print("Debug: " + guestName, guestsItem)'''

# Automatically generate and print the list of items
items_set = set()
for guestItems in guestDictionary.values():
    for item in guestItems.keys():
        items_set.add(item)

print('\n\n\nNumber of things being brought:')
for item in items_set:
    print(f' - {item.capitalize().replace("_", " ")}.........' + str(totalBrought(guestDictionary, item)))