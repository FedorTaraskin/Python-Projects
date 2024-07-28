#! python3
from argparse import ArgumentParser
#mclip.py - A multi-clipboard program.
##Newer version

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

def listPrinter(value): ##If value is a dictionary, makes a list out of the keys.
	toReturn = str(list(value))
	toReturn = toReturn.replace("[", "")
	toReturn = toReturn.replace("]", "")
	toReturn = toReturn.replace("'", "")
	return toReturn

parser = ArgumentParser(description = 'mclip.py - A multi-clipboard program.')
parser.add_argument('-mode', '--mode', required=True, help='Mode selection. Can be write or read ("w" or "r").')
parser.add_argument('-title', '--title', required=True, help='Title for the copypasta.')
args = parser.parse_args()
del parser

if args.mode == 'w':
	TEXT.update({args.title: str(input('What text would you like to add?: '))})
	print(f'The new database is:\n{TEXT}')
elif args.mode == 'r':
	print(TEXT.get(args.title, f"This does not exist yet.\nAvailable options are: {listPrinter(TEXT)}"))
input()