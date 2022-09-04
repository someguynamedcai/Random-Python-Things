import random 

#Choosing first or second
def chooseturn():
    while (True):
        side = input("Would you like to go first or second? ")
        if (side == "First" or side == "first" or side == "f" or side == "1"):
            print ("You have chosen to start first.")
            side = 1
            return side
        elif (side == "Second" or side == "second" or side =="s" or side == "2"):
            print ("You have chosen to start second.")
            side = 2
            return side
        else:
            print ("Invalid input. Please try again.")

def choosepiece():
    while (True):
        xo = input("Would you like to be X or O? ")
        if (xo == "X" or xo == "x"):
            print ("You have chosen X.")
            xo = "X"
            return xo;
        elif (xo == "O" or xo == "o"):
            print ("You have chosen O.")
            xo = "O"
            return xo;
        else:
            print ("Invalid input. Please try again.")
        
def printboard():
    print ("\n")
    j = 0
    for i in range(3):
        print ("[" + str(board[i+j]) + "|" + str(board[i+j+1])+ "|" + str(board[i+j+2]) + "]")
        j+=2
    print ("\n")

def resetboard(board):
    for i in range(10):
        board[i] = i
    return board

def Valid(num):
    if (board[num] == "X" or board[num] == "O"):
        return False
    else:
        return True

def checkEnd(side, xo):
    if board[0] == xo and board[1] == xo and board[2] == xo:
        print(str(xo) + " " + str(side))
        return side
    elif board[3] == xo and board[4] == xo and board[5] == xo:
        return side
    elif board[6] == xo and board[7] == xo and board[8] == xo:
        return side
    elif board[0] == xo and board[3] == xo and board[6] == xo:
        return side
    elif board[1] == xo and board[4] == xo and board[7] == xo:
        return side
    elif board[2] == xo and board[5] == xo and board[8] == xo:
        return side
    elif board[0] == xo and board[4] == xo and board[8] == xo:
        return side
    elif board[2] == xo and board[4] == xo and board[6] == xo:
        return side
    else:
        return -1

def play(win,wtally,ltally,ttally):
    side = chooseturn()
    xo = choosepiece()
    moves = 0
    while (moves != 9):
        printboard()
        print (win)
        if (win == 1):
            wtally+=1
            print ("You have won!")
            return True
        elif (win == 2):
            ltally+=1
            print ("You have lost.")
            return False
        else:
            if side == 1:
                try:
                    turn = int(input("Choose a number to place a piece on the board: "))
                    if Valid(turn) == True:
                        board[turn] = xo
                        print ("You have placed a " + xo + " on number " + str(turn))
                        win = checkEnd(side,xo)
                        side = 2
                        if (xo =="X"):
                            xo = "O"
                        else:
                            xo = "X"
                        moves+=1
                    else:
                        print ("That move is invalid. Choose another number.")
                except ValueError:
                    print ("Invalid input. Try again.")
            else:
                while (True):
                    turn = random.randrange(9)
                    if Valid(turn):
                        board[turn] = xo
                        print ("The AI places " + xo + " on " + str(turn) + ".")
                        win = checkEnd(side,xo)
                        side = 1
                        xo = "X"
                        moves+=1
                        break;
    printboard()
    print ("It is a tie.")
    return
board = [i for i in range(10)]
win = -1
wtally=0
ltally=0
ttally=0
while(True):
    result = play(win,wtally,ltally,ttally)
    if (result == True):
        wtally+=1
    elif (result == False):
        ltally+=1
    else:
        ttally+=1
        
    print ("You currently have " + str(wtally) + " wins, " + str(ltally) + " losses, and " + str(ttally) + " ties.")
    again = input("Would you like to play again? ")
    try:
        if (again == "yes" or again == "Yes" or again == "Y" or again == "y"):
            print ("A new game will start.")
            resetboard(board)
            play()
        else:
            print ("The game will close.")
            break
    except ValueError:
        print ("The game will close.")
        break;



