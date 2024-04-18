# hi thx for reading my code

# clears screen
import os
os.system("cls")

# all games stuff
game = ""

# checkers stuff
black = "0"
white = "O"
empty = "+"
eight = [empty, black, empty, black, empty, black, empty, black]
seven = [black, empty, black, empty, black, empty, black, empty]
six = [empty, black, empty, black, empty, black, empty, black]
five = [empty, empty, empty, empty, empty, empty, empty, empty]
four = [empty, empty, empty, empty, empty, empty, empty, empty]
three = [white, empty, white, empty, white, empty, white, empty]
two = [empty, white, empty, white, empty, white, empty, white]
one = [white, empty, white, empty, white, empty, white, empty]
letterIndex = ["A", "B", "C", "D", "E", "F", "G", "H"]

# tic tac toe stuff
x = "X"
o = "O"
space = " "
tictactoe3 = [space, space, space]
tictactoe2 = [space, space, space]
tictactoe1 = [space, space, space]
tictacLetterIndex = ["A", "B", "C"]

# re-prints the ckeckers board
def updateCheckerboard():
    os.system("cls")
    print("8    " + eight[0] + "  " + eight[1] + "  " + eight[2] + "  " + eight[3] + "  " + eight[4] + "  " + eight[5] + "  " + eight[6] + "  " + eight[7])
    print("7    " + seven[0] + "  " + seven[1] + "  " + seven[2] + "  " + seven[3] + "  " + seven[4] + "  " + seven[5] + "  " + seven[6] + "  " + seven[7])
    print("6    " + six[0] + "  " + six[1] + "  " + six[2] + "  " + six[3] + "  " + six[4] + "  " + six[5] + "  " + six[6] + "  " + six[7])
    print("5    " + five[0] + "  " + five[1] + "  " + five[2] + "  " + five[3] + "  " + five[4] + "  " + five[5] + "  " + five[6] + "  " + five[7])
    print("4    " + four[0] + "  " + four[1] + "  " + four[2] + "  " + four[3] + "  " + four[4] + "  " + four[5] + "  " + four[6] + "  " + four[7])
    print("3    " + three[0] + "  " + three[1] + "  " + three[2] + "  " + three[3] + "  " + three[4] + "  " + three[5] + "  " + three[6] + "  " + three[7])
    print("2    " + two[0] + "  " + two[1] + "  " + two[2] + "  " + two[3] + "  " + two[4] + "  " + two[5] + "  " + two[6] + "  " + two[7])
    print("1    " + one[0] + "  " + one[1] + "  " + one[2] + "  " + one[3] + "  " + one[4] + "  " + one[5] + "  " + one[6] + "  " + one[7])
    print("")
    print("     " + letterIndex[0] + "  " + letterIndex[1] + "  " + letterIndex[2] + "  " + letterIndex[3] + "  " + letterIndex[4] + "  " + letterIndex[5] + "  " + letterIndex[6] + "  " + letterIndex[7] + F"       * black pieces are '{black}' and white pieces are '{white}'")

def checkLegalMove(currentTurn, moveInput):
    correctlySelected = False
    moveSpotOpen = False
    validRegularMoveY = False
    validRegularMoveX = False
    validJumpingMove = False
    if currentTurn == "white":
        if moveInput[1] == "1":
            correctlySelected = (one[letterIndex.index(moveInput[0])] == white)
        elif moveInput[1] == "2":
            correctlySelected = (two[letterIndex.index(moveInput[0])] == white)
        elif moveInput[1] == "3":
            correctlySelected = (three[letterIndex.index(moveInput[0])] == white)
        elif moveInput[1] == "4":
            correctlySelected = (four[letterIndex.index(moveInput[0])] == white)
        elif moveInput[1] == "5":
            correctlySelected = (five[letterIndex.index(moveInput[0])] == white)
        elif moveInput[1] == "6":
            correctlySelected = (six[letterIndex.index(moveInput[0])] == white)
        elif moveInput[1] == "7":
            correctlySelected = (seven[letterIndex.index(moveInput[0])] == white)
        elif moveInput[1] == "8":
            correctlySelected = (eight[letterIndex.index(moveInput[0])] == white)
        else:
            correctlySelected = False
    elif currentTurn == "black":
        if moveInput[1] == "1":
            correctlySelected = (one[letterIndex.index(moveInput[0])] == black)
        elif moveInput[1] == "2":
            correctlySelected = (two[letterIndex.index(moveInput[0])] == black)
        elif moveInput[1] == "3":
            correctlySelected = (three[letterIndex.index(moveInput[0])] == black)
        elif moveInput[1] == "4":
            correctlySelected = (four[letterIndex.index(moveInput[0])] == black)
        elif moveInput[1] == "5":
            correctlySelected = (five[letterIndex.index(moveInput[0])] == black)
        elif moveInput[1] == "6":
            correctlySelected = (six[letterIndex.index(moveInput[0])] == black)
        elif moveInput[1] == "7":
            correctlySelected = (seven[letterIndex.index(moveInput[0])] == black)
        elif moveInput[1] == "8":
            correctlySelected = (eight[letterIndex.index(moveInput[0])] == black)
        else:
            correctlySelected = False
    else:
        correctlySelected = False
    # checks if the currently selected checker is good to move

    if moveInput[4] == "1":
        moveSpotOpen = (one[letterIndex.index(moveInput[3])] == empty)
    elif moveInput[4] == "2":
        moveSpotOpen = (two[letterIndex.index(moveInput[3])] == empty)
    elif moveInput[4] == "3":
        moveSpotOpen = (three[letterIndex.index(moveInput[3])] == empty)
    elif moveInput[4] == "4":
        moveSpotOpen = (four[letterIndex.index(moveInput[3])] == empty)
    elif moveInput[4] == "5":
        moveSpotOpen = (five[letterIndex.index(moveInput[3])] == empty)
    elif moveInput[4] == "6":
        moveSpotOpen = (six[letterIndex.index(moveInput[3])] == empty)
    elif moveInput[4] == "7":
        moveSpotOpen = (seven[letterIndex.index(moveInput[3])] == empty)
    elif moveInput[4] == "8":
        moveSpotOpen = (eight[letterIndex.index(moveInput[3])] == empty)
    else:
        moveSpotOpen = False
    # checks if the spot the selected checker will move to is open

    if currentTurn == "white":
        if moveInput[1] == "1":
            validRegularMoveY = (moveInput[4] == "2")
        if moveInput[1] == "2":
            validRegularMoveY = (moveInput[4] == "3")
        if moveInput[1] == "3":
            validRegularMoveY = (moveInput[4] == "4")
        if moveInput[1] == "4":
            validRegularMoveY = (moveInput[4] == "5")
        if moveInput[1] == "5":
            validRegularMoveY = (moveInput[4] == "6")
        if moveInput[1] == "6":
            validRegularMoveY = (moveInput[4] == "7")
        if moveInput[1] == "7":
            validRegularMoveY = (moveInput[4] == "8")
        if moveInput[1] == "8":
            validRegularMoveY = False
    elif currentTurn == "black":
        if moveInput[1] == "8":
            validRegularMoveY = (moveInput[4] == "7")
        if moveInput[1] == "7":
            validRegularMoveY = (moveInput[4] == "6")
        if moveInput[1] == "6":
            validRegularMoveY = (moveInput[4] == "5")
        if moveInput[1] == "5":
            validRegularMoveY = (moveInput[4] == "4")
        if moveInput[1] == "4":
            validRegularMoveY = (moveInput[4] == "3")
        if moveInput[1] == "3":
            validRegularMoveY = (moveInput[4] == "2")
        if moveInput[1] == "2":
            validRegularMoveY = (moveInput[4] == "1")
        if moveInput[1] == "1":
            validRegularMoveY = False
    else:
        validRegularMoveY = False
    # checks if the y pos (number axis) of the move is acceptable, assuming it is a non-jumping move

    validRegularMoveX = abs(int(letterIndex.index(moveInput[0])) - int(letterIndex.index(moveInput[3]))) == 1
    # checks if the x pos (letter axis) of the move is acceptable, assuming it is a non-jumping move

    return correctlySelected and moveSpotOpen and ((validRegularMoveY and validRegularMoveX) or validJumpingMove)

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
                if checkLegalMove(turn, move):
                    if move[1] == "1":
                        one[letterIndex.index(move[0])] = empty
                    elif move[1] == "2":
                        two[letterIndex.index(move[0])] = empty
                    elif move[1] == "3":
                        three[letterIndex.index(move[0])] = empty
                    elif move[1] == "4":
                        four[letterIndex.index(move[0])] = empty
                    elif move[1] == "5":
                        five[letterIndex.index(move[0])] = empty
                    elif move[1] == "6":
                        six[letterIndex.index(move[0])] = empty
                    elif move[1] == "7":
                        seven[letterIndex.index(move[0])] = empty
                    elif move[1] == "8":
                        eight[letterIndex.index(move[0])] = empty
                    else:
                        os.system("cls")
                        print("game is broke :(")
                    # clears previous position
                    if turn == "white":
                        if move[4] == "1":
                            one[letterIndex.index(move[3])] = white
                        elif move[4] == "2":
                            two[letterIndex.index(move[3])] = white
                        elif move[4] == "3":
                            three[letterIndex.index(move[3])] = white
                        elif move[4] == "4":
                            four[letterIndex.index(move[3])] = white
                        elif move[4] == "5":
                            five[letterIndex.index(move[3])] = white
                        elif move[4] == "6":
                            six[letterIndex.index(move[3])] = white
                        elif move[4] == "7":
                            seven[letterIndex.index(move[3])] = white
                        elif move[4] == "8":
                            eight[letterIndex.index(move[3])] = white
                        else:
                            os.system("cls")
                            print("game is broke :(")
                    elif turn == "black":
                        if move[4] == "1":
                            one[letterIndex.index(move[3])] = black
                        elif move[4] == "2":
                            two[letterIndex.index(move[3])] = black
                        elif move[4] == "3":
                            three[letterIndex.index(move[3])] = black
                        elif move[4] == "4":
                            four[letterIndex.index(move[3])] = black
                        elif move[4] == "5":
                            five[letterIndex.index(move[3])] = black
                        elif move[4] == "6":
                            six[letterIndex.index(move[3])] = black
                        elif move[4] == "7":
                            seven[letterIndex.index(move[3])] = black
                        elif move[4] == "8":
                            eight[letterIndex.index(move[3])] = black
                        else:
                            os.system("cls")
                            print("game is broke :(")
                    else:
                            os.system("cls")
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
        if (white not in one) and (white not in two) and (white not in three) and (white not in four) and (white not in five) and (white not in six) and (white not in seven) and (white not in eight):
            winner = "black"
            break
        elif (black not in one) and (black not in two) and (black not in three) and (black not in four) and (black not in five) and (black not in six) and (black not in seven) and (black not in eight):
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
    os.system("cls")
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
                            os.system("cls")
                            print("game is broke :(")
                    elif turn == "O":
                        if move[1] == "1":
                           tictactoe1[tictacLetterIndex.index(move[0])] = o
                        elif move[1] == "2":
                            tictactoe2[tictacLetterIndex.index(move[0])] = o
                        elif move[1] == "3":
                           tictactoe3[tictacLetterIndex.index(move[0])] = o
                        else:
                            os.system("cls")
                            print("game is broke :(")
                    else:
                        os.system("cls")
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