# hi thx for reading my code

import os

# all games stuff
game = ""

# checkers stuff
black = "0"
white = "O"
empty = "+"
board = (
    [empty, black, empty, black, empty, black, empty, black],
    [black, empty, black, empty, black, empty, black, empty],
    [empty, black, empty, black, empty, black, empty, black],
    [empty, empty, empty, empty, empty, empty, empty, empty],
    [empty, empty, empty, empty, empty, empty, empty, empty],
    [white, empty, white, empty, white, empty, white, empty],
    [empty, white, empty, white, empty, white, empty, white],
    [white, empty, white, empty, white, empty, white, empty],
)
letterIndex = ["A", "B", "C", "D", "E", "F", "G", "H"]

# tic tac toe stuff
x = "X"
o = "O"
space = " "
tictactoe3 = [space, space, space]
tictactoe2 = [space, space, space]
tictactoe1 = [space, space, space]
tictacLetterIndex = ["A", "B", "C"]

def clear():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

# re-prints the ckeckers board
def updateCheckerboard():
    clear()
    print("8    " + board[0][0] + "  " + board[0][1] + "  " + board[0][2] + "  " + board[0][3] + "  " + board[0][4] + "  " + board[0][5] + "  " + board[0][6] + "  " + board[0][7])
    print("7    " + board[1][0] + "  " + board[1][1] + "  " + board[1][2] + "  " + board[1][3] + "  " + board[1][4] + "  " + board[1][5] + "  " + board[1][6] + "  " + board[1][7])
    print("6    " + board[2][0] + "  " + board[2][1] + "  " + board[2][2] + "  " + board[2][3] + "  " + board[2][4] + "  " + board[2][5] + "  " + board[2][6] + "  " + board[2][7])
    print("5    " + board[3][0] + "  " + board[3][1] + "  " + board[3][2] + "  " + board[3][3] + "  " + board[3][4] + "  " + board[3][5] + "  " + board[3][6] + "  " + board[3][7])
    print("4    " + board[4][0] + "  " + board[4][1] + "  " + board[4][2] + "  " + board[4][3] + "  " + board[4][4] + "  " + board[4][5] + "  " + board[4][6] + "  " + board[4][7])
    print("3    " + board[5][0] + "  " + board[5][1] + "  " + board[5][2] + "  " + board[5][3] + "  " + board[5][4] + "  " + board[5][5] + "  " + board[5][6] + "  " + board[5][7])
    print("2    " + board[6][0] + "  " + board[6][1] + "  " + board[6][2] + "  " + board[6][3] + "  " + board[6][4] + "  " + board[6][5] + "  " + board[6][6] + "  " + board[6][7])
    print("1    " + board[7][0] + "  " + board[7][1] + "  " + board[7][2] + "  " + board[7][3] + "  " + board[7][4] + "  " + board[7][5] + "  " + board[7][6] + "  " + board[7][7])
    print("")
    print("     " + letterIndex[0] + "  " + letterIndex[1] + "  " + letterIndex[2] + "  " + letterIndex[3] + "  " + letterIndex[4] + "  " + letterIndex[5] + "  " + letterIndex[6] + "  " + letterIndex[7] + F"       * black pieces are '{black}' and white pieces are '{white}'")

def checkLegalMove(currentTurn, moveInput, move1, move4):
    
    correctlySelected = False
    moveSpotOpen = False
    validRegularMoveX = False
    validRegularMoveY = False
    validJumpingMoveX = False
    validJumpingMoveY = False
    validPieceForJump = False
    jumpedPiece = ""

    if currentTurn == "white":
        correctlySelected = (board[move1][letterIndex.index(moveInput[0])] == white)
    elif currentTurn == "black":
        correctlySelected = (board[move1][letterIndex.index(moveInput[0])] == black)
    else:
        correctlySelected = False
    # checks if the currently selected checker is good to move

    moveSpotOpen = (board[move4 - 1][letterIndex.index(moveInput[3])] == empty)
    # checks if the spot the selected checker will move to is open

    if currentTurn == "white":
        if moveInput[1] == "1":
            validRegularMoveY = (moveInput[4] == "2")
        elif moveInput[1] == "2":
            validRegularMoveY = (moveInput[4] == "3")
        elif moveInput[1] == "3":
            validRegularMoveY = (moveInput[4] == "4")
        elif moveInput[1] == "4":
            validRegularMoveY = (moveInput[4] == "5")
        elif moveInput[1] == "5":
            validRegularMoveY = (moveInput[4] == "6")
        elif moveInput[1] == "6":
            validRegularMoveY = (moveInput[4] == "7")
        elif moveInput[1] == "7":
            validRegularMoveY = (moveInput[4] == "8")
        elif moveInput[1] == "8":
            validRegularMoveY = False
        else:
            validRegularMoveY = False
    elif currentTurn == "black":
        if moveInput[1] == "8":
            validRegularMoveY = (moveInput[4] == "7")
        elif moveInput[1] == "7":
            validRegularMoveY = (moveInput[4] == "6")
        elif moveInput[1] == "6":
            validRegularMoveY = (moveInput[4] == "5")
        elif moveInput[1] == "5":
            validRegularMoveY = (moveInput[4] == "4")
        elif moveInput[1] == "4":
            validRegularMoveY = (moveInput[4] == "3")
        elif moveInput[1] == "3":
            validRegularMoveY = (moveInput[4] == "2")
        elif moveInput[1] == "2":
            validRegularMoveY = (moveInput[4] == "1")
        elif moveInput[1] == "1":
            validRegularMoveY = False
        else:
            validRegularMoveY = False
    else:
        validRegularMoveY = False
    # checks if the y pos (number axis) of the move is acceptable, assuming it is a non-jumping move

    validRegularMoveX = abs(int(letterIndex.index(moveInput[0])) - int(letterIndex.index(moveInput[3]))) == 1
    # checks if the x pos (letter axis) of the move is acceptable, assuming it is a non-jumping move

    if not (validRegularMoveX and validRegularMoveY):
        if currentTurn == "white":
            if moveInput[1] == "1":
                validJumpingMoveY = (moveInput[4] == "3")
            elif moveInput[1] == "2":
               validJumpingMoveY = (moveInput[4] == "4")
            elif moveInput[1] == "3":
                validJumpingMoveY = (moveInput[4] == "5")
            elif moveInput[1] == "4":
                validJumpingMoveY = (moveInput[4] == "6")
            elif moveInput[1] == "5":
                validJumpingMoveY = (moveInput[4] == "7")
            elif moveInput[1] == "6":
                validJumpingMoveY = (moveInput[4] == "8")
            elif moveInput[1] == "7":
                validJumpingMoveY = False
            elif moveInput[1] == "8":
                validJumpingMoveY = False
            else:
                validJumpingMoveY = False
        elif currentTurn == "black":
            if moveInput[1] == "8":
                validJumpingMoveY = (moveInput[4] == "6")
            elif moveInput[1] == "7":
                validJumpingMoveY = (moveInput[4] == "5")
            elif moveInput[1] == "6":
                validJumpingMoveY = (moveInput[4] == "4")
            elif moveInput[1] == "5":
                validJumpingMoveY = (moveInput[4] == "3")
            elif moveInput[1] == "4":
                validJumpingMoveY = (moveInput[4] == "2")
            elif moveInput[1] == "3":
                validJumpingMoveY = (moveInput[4] == "1")
            elif moveInput[1] == "2":
                validJumpingMoveY = False
            elif moveInput[1] == "1":
                validJumpingMoveY = False
            else:
                validJumpingMoveY = False
        else:
            validJumpingMoveY = False
        # checks if the y pos (number axis) of the move is acceptable, assuming it is a jumping move

        validJumpingMoveX = abs(int(letterIndex.index(moveInput[0])) - int(letterIndex.index(moveInput[3]))) == 2
        # checks if the x pos (letter axis) of the move is acceptable, assuming it is a jumping move
        
        if currentTurn == "white":
            if board[move1 - 2][int((letterIndex.index(moveInput[3]) + letterIndex.index(moveInput[0])) / 2)] == black:
                validPieceForJump = True
                jumpedPiece = letterIndex[int((letterIndex.index(moveInput[3]) + letterIndex.index(moveInput[0])) / 2)] + "1"
        elif currentTurn == "black":
            if board[move1 - 1][int((letterIndex.index(moveInput[3]) + letterIndex.index(moveInput[0])) / 2)] == white:
                validPieceForJump = True
                jumpedPiece = letterIndex[int((letterIndex.index(moveInput[3]) + letterIndex.index(moveInput[0])) / 2)] + "2"
        else:
            validPieceForJump = False
        # makes sure the jumped piece is valid.

        if correctlySelected and moveSpotOpen and (validJumpingMoveX and validJumpingMoveY and validPieceForJump):
                board[move1 - 1][letterIndex.index(jumpedPiece[0])] = empty

    # print("correctlySelected: " + str(correctlySelected) + " moveSpotOpen: " + str(moveSpotOpen) + " validRegularMoveX: " + str(validRegularMoveX) + " validRegularMoveY: " + str(validRegularMoveY) + " validJumpingMoveX: " + str(validJumpingMoveX) + " validJumpingMoveY: " + str(validJumpingMoveY) + " validPieceForJump: " + str(validPieceForJump))
    # for debugging ^
    return correctlySelected and moveSpotOpen and ((validRegularMoveY and validRegularMoveX) or (validJumpingMoveX and validJumpingMoveY and validPieceForJump))

# plays checkers
def checkers():
    turn = "white"
    winner = ""
    ready = (input("Checkers: Move diagonally and jump over pieces to take them. (double jumping is not allowed). Press enter to play!"))
    updateCheckerboard()
    print("")
    while winner == "":
        move = ""
        while move == "":
            move = input(F"It is {turn}'s turn. Please enter the location of a {turn} piece and a valid place to move it. Format example: 'A3 B4'.  ").upper()
            if (len(move) == 5) and (move[0] in letterIndex) and (move[3] in letterIndex) and (move[1].isnumeric() and (int(move[1]) >= 1 and int(move[1]) <= 8)) and (move[4].isnumeric() and (int(move[4]) >= 1 and int(move[4]) <= 8)):
                move1 = 8 - int(move[1])
                move4 =  8 - int(move[4])
                if checkLegalMove(turn, move, move1, move4):
                    board[move1][letterIndex.index(move[0])] = empty
                    # clears previous position
                    if turn == "white":
                        board[move4][letterIndex.index(move[3])] = white
                    elif turn == "black":
                        board[move4][letterIndex.index(move[3])] = black
                    else:
                            clear()
                            print("game is broke :(")
                    # moves to new position
                else:
                    print("uh oh, that move is invalid... please try again!")
                    move = ""
            else:
                print("uh oh, you formatted something incorrectly... please try again!")
                move = ""
        updateCheckerboard()
        print("")
        if (white not in board[0]) and (white not in board[1]) and (white not in board[2]) and (white not in board[3]) and (white not in board[4]) and (white not in board[5]) and (white not in board[6]) and (white not in board[7]):
            winner = "black"
            break
        elif (black not in board[0]) and (black not in board[1]) and (black not in board[2]) and (black not in board[3]) and (black not in board[4]) and (black not in board[5]) and (black not in board[6]) and (black not in board[7]):
            winner = "white"
            break
        else:
            winner = ""
        if turn == "white":
            turn = "black"
        elif turn == "black":
            turn = "white"
    print(F"congrats {winner}, you won!")

def updateTicTacToeBoard():
    clear()
    print("3  " + tictactoe3[0] + " | " + tictactoe3[1] + " | " + tictactoe3[2])
    print("  ———————————")
    print("2  " + tictactoe2[0] + " | " + tictactoe2[1] + " | " + tictactoe2[2])
    print("  ———————————")
    print("1  " + tictactoe1[0] + " | " + tictactoe1[1] + " | " + tictactoe1[2])
    print("   " + tictacLetterIndex[0] + "   " + tictacLetterIndex[1] + "   " + tictacLetterIndex[2])

def spotOpenTicTacToe(moveInput):
    if moveInput[1] == "1":
        return tictactoe1[tictacLetterIndex.index(moveInput[0])] == space
    elif moveInput[1] == "2":
        return tictactoe2[tictacLetterIndex.index(moveInput[0])] == space
    elif moveInput[1] == "3":
        return tictactoe3[tictacLetterIndex.index(moveInput[0])] == space
    else:
        return False
    
def checktictactoewinner(symbol):
    across = False
    down = False
    diagonal = False
    across = (tictactoe1[0] == symbol and tictactoe1[1] == symbol and tictactoe1[2] == symbol) or (tictactoe2[0] == symbol and tictactoe2[1] == symbol and tictactoe2[2] == symbol) or (tictactoe3[0] == symbol and tictactoe3[1] == symbol and tictactoe3[2] == symbol)
    down = (tictactoe1[0] == symbol and tictactoe2[0] == symbol and tictactoe3[0] == symbol) or (tictactoe1[1] == symbol and tictactoe2[1] == symbol and tictactoe3[1] == symbol) or (tictactoe1[2] == symbol and tictactoe2[2] == symbol and tictactoe3[2] == symbol)
    diagonal = (tictactoe1[0] == symbol and tictactoe2[1] == symbol and tictactoe3[2] == symbol) or (tictactoe1[2] == symbol and tictactoe2[1] == symbol and tictactoe3[0] == symbol)
    return across or down or diagonal

def tictactoe():
    winner = ""
    turn = "X"
    ready = (input("Tic Tac Toe: Enter the coordinate of the section you want to place your marker in. Get three in a row to win! Press enter to play!"))
    updateTicTacToeBoard()
    print("")
    while winner == "":
        move = ""
        while move == "":
            move = input(F"It is {turn}'s turn. Please enter where you would like to place the piece. Format example: 'B2'.  ").upper()
            if (len(move) == 2) and (move[1].isnumeric()) and (move[0] in tictacLetterIndex) and (int(move[1]) >= 1) and (int(move[1]) <= 3):
                if spotOpenTicTacToe(move):
                    if turn == "X":
                        if move[1] == "1":
                           tictactoe1[tictacLetterIndex.index(move[0])] = x
                        elif move[1] == "2":
                            tictactoe2[tictacLetterIndex.index(move[0])] = x
                        elif move[1] == "3":
                           tictactoe3[tictacLetterIndex.index(move[0])] = x
                        else:
                            clear()
                            print("game is broke :(")
                    elif turn == "O":
                        if move[1] == "1":
                           tictactoe1[tictacLetterIndex.index(move[0])] = o
                        elif move[1] == "2":
                            tictactoe2[tictacLetterIndex.index(move[0])] = o
                        elif move[1] == "3":
                           tictactoe3[tictacLetterIndex.index(move[0])] = o
                        else:
                            clear()
                            print("game is broke :(")
                    else:
                        clear()
                        print("game is broke :(")
                else:
                    print("uh oh, that move is invalid... please try again!")
                    move = ""
            else:
                print("uh oh, you formatted something incorrectly... please try again!")
                move = ""
        updateTicTacToeBoard()
        print("")
        if checktictactoewinner(o):
            winner = "O"
            break
        elif checktictactoewinner(x):
            winner = "X"
            break
        elif (space not in tictactoe1) and (space not in tictactoe2) and (space not in tictactoe3):
            winner = "tie"
            break
        else:
            winner = ""
        if turn == "O":
            turn = "X"
        elif turn == "X":
            turn = "O"
    print(F"congrats {winner}, you won!")


# beginning of game
clear()
print("GREETINGS, and Welcome to V.I.G. (or Very Impractical Games)!")
while True:
    game = input("So far, we have 'checkers' and 'tic tac toe'. Which game would you like to play?  ")
    if game == "checkers":
        checkers()
        break
    elif game == "tic tac toe":
        tictactoe()
        break
    else:
        print("Sorry, we don't have '%s', or you may have typed it wrong. Please try again." % game)