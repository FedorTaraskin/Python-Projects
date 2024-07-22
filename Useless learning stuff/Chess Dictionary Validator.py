##Note: this only checks if there are too many of the same pieces or not, as well as whether pieces are on non-exitant places.
##Doesn't check for any other chess rules.

##myChessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3m': 'wking', '4f': 'bking'}
myChessBoard = {
	'4d': 'wking',   # White king at 4d
	'8a': 'brook',   # Black rook at 8a
	'1f': 'wpawn',   # White pawn at 1f
	'3c': 'bbishop', # Black bishop at 3c
	'7h': 'wrook'    # White rook at 7h
}

def isValidChessBoard(board): ##The main function, made to be inserted into another program.
	##Prep
	pieceMaxAmounts = {"king": 1, "queen": 1, "rook": 2, "knight": 2, "bishop": 2, "pawn": 8} ##Only for a single color.
	#totalPieceMaxAmount = 16 ##Only for a single color.
	pieceTranslations = {}
	englishPieceNames = ("King", "Queen", "Rook", "Knight", "Bishop", "Pawn")
	pieceInstancesValidationResults = {}
	for i in englishPieceNames: ##Makes a translation dictionary
		i = i.lower() ##Feeling too lazy to rewrite line 10 lol
		pieceTranslations["w" + i] = "White " + i
		pieceTranslations["b" + i] = "Black " + i
	del englishPieceNames

	def validAmountOfSpecificPieceInstances(boardDictionary, pieceToCheck): ##Checks the amount of just one piece, pieceToCheck
		pieceAmount = 0
		maxPieceAmount = pieceMaxAmounts[pieceToCheck[1:]]
		boardValues = tuple(boardDictionary.values())
		for i in range(len(boardDictionary)):
			if pieceToCheck in boardValues[i]:
				pieceAmount += 1
		
		if pieceAmount > maxPieceAmount:
			return False
		elif pieceAmount <= maxPieceAmount:
			return True
		else:
			print("Something unexpected happened.")

	'''def validAmountOfPieceInstantes(boardDictionary, colorToCheck): ##Checks whether there's too many piece of the same color
		colorsPieces = [] ##colorToCheck can be either w or b
		boardValues = tuple(boardDictionary.values())
		for i in boardValues:
			if i[:1] == colorToCheck:
				colorsPieces += i
				'''

	def validPiecePositions(boardDictionary, pieceToCheck): ##Cheks whether the passed piece is on a valid position
		## 1 to 8, A to H
		## i is the piece being checked
		acceptable = ("12345678abcdefgh")

		## Extract the key associated with the piece
		for k, value in boardDictionary.items():
			if value == pieceToCheck:
				break

		## Check if the key is not in acceptable
		if k is not None and k[1:] not in acceptable:
			return False
		if k is not None and k[:1] not in acceptable:
			return False
		else:
			return True

	def validKingAmounts(boardDictionary):
		wKingAmount = 0
		bKingAmount = 0
		for i in boardDictionary.values():
			if i == "wking":
				wKingAmount += 1
			elif i == "bking":
				bKingAmount += 1

		if wKingAmount == 1 and bKingAmount == 1:
			return True
		else:
			return False

	try:
		##Checking for positions and piece amounts (except-ish kings)*, using previous functions.
		for piece in board.values():
			pieceValidationResult = validAmountOfSpecificPieceInstances(board, piece) and validPiecePositions(board, piece)

			if piece not in pieceInstancesValidationResults: ##There's probably a way to optimize this by not using dictionaries..
				pieceInstancesValidationResults[piece] = pieceValidationResult

			#print(pieceTranslations[piece] + " returned " + str(pieceInstancesValidationResults[piece]))

		if False in pieceInstancesValidationResults.values():
			return False, "one of the pieces has wrong data."
		elif validKingAmounts(myChessBoard) == False:
			return False, "there is a king missing."
		elif False not in pieceInstancesValidationResults.values():
			return True, "everything seems right... as far as this program can tell, anyways."
	except:
		return False, "incorrect piece name."
	
	## Add a default return statement here (so that the compiler doesn't whine)
	return False, "unknown error."
		
finalResult, reason = isValidChessBoard(myChessBoard)
print("\nThe final result is " + str(finalResult) + " for the reason: " + str(reason))

## *checks whether there are too many kings, but doesn't check whether there's exactly one.