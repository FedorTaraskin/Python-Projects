#! python3
import sys
# mclip.py - A multi-clipboard program.
##Abandoned, I discovered the argparse module. https://chatgpt.com/share/e6a0a4ec-ad5b-4414-b9cf-ea82285e4efc


TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


while (len(sys.argv)) != 2 or (sys.argv[1] not in TEXT.keys()): ##Messed up logic -- TODO

	if len(sys.argv) < 2:
		print('Usage: python mcpclip.py [keyphrase] - copies phrase text.')

	elif sys.argv not in TEXT:
		choice = input("That is not a correct argument. Would you like to get a list of all posible arguments? Y/N: ")
		choice = ''
		while choice != "N":
			if choice == "Y":
				print(TEXT.keys)
				break
input()