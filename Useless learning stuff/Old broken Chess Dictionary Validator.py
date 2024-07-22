##Note: this only checks if there are too many of the same pieces or not.
##Doesn't check for any other chess rules.
myChessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4f': 'bking'}

def isValidChessBoard(board):
    pieceMaxAmounts = {"king": 1, "queen": 1, "rook": 2, "knight": 2, "bishop": 2, "pawn": 8} ##Only for a single color.
    pieceTranslations = {}
    englishPieceNames = ("King", "Queen", "Rook", "Knight", "Bishop", "Pawn")
    pieceValidationResults = {}
    for i in englishPieceNames:
        i = i.lower() ##Feeling too lazy to rewrite line 10 lol
        pieceTranslations["w" + i] = "White " + i
        pieceTranslations["b" + i] = "Black " + i

    #board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '4f': 'bking'}

    def validAmountOfPieceInstances(boardDictionary, pieceToCheck, maxPieceAmount):
        pieceAmount = 0
        temp1 = list(boardDictionary.values())
        for i in range(len(boardDictionary)):
            if pieceToCheck in temp1[i]:
                pieceAmount += 1
        
        if pieceAmount > maxPieceAmount:
            return False
        elif pieceAmount <= maxPieceAmount:
            return True
        else:
            print("Something unexpected happened.")
    
    def validPiecePositions(boardDictionary):
        ## 1 to 8, A to H
        badCharacters = [chr(i) for i in range(32, 127) if chr(i) not in 'ABCDEFGH']
        for i in board:
            if badCharacters in board: ## ERROR HERE
                returnTrue = False
                return False
        if returnTrue != False:
            return True
        
    print(validPiecePositions(board))

    for piece in board.values():
        pieceValidationResult = validAmountOfPieceInstances(board, piece, pieceMaxAmounts[piece[1:]])
            
        '''if pieceValidationResult == True and piece not in pieceValidationResults:
            print("The " + pieceTranslations[piece] + " piece appears a valid amount of times.", end=" ")
        elif pieceValidationResult == False and piece not in pieceValidationResults:
            print("The " + pieceTranslations[piece] + " piece DOES NOT appear a valid amount of times.", end=" ")'''

        if piece not in pieceValidationResults: #There's probably a way to optimize this by not using dictionaries..
            pieceValidationResults[piece] = pieceValidationResult
        
        #print("No other pieces appear.")
    
    if False in pieceValidationResults:
        return False
    elif False not in pieceValidationResults:
        return True
        
print(isValidChessBoard(myChessBoard))