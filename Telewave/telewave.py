import random 

#check how many lines are in clue list 
def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

#Playing the game
def Play(filename,randnum,correctnum,currentteam,maxclue,maxmulligan):
    mull = 0
    print ("Team " + str(currentteam+1) + " is up.")
    print ("Your clue is " + str(filename[randnum]))
    while (True):
        mulligan = input("Do you want another clue: ")
        if maxmulligan-mull == 0:
            print ("You have ran out of mulligans.")
            randnum = Mulligan(maxclue)
            print ("Your clue is " + str(filename[randnum]))
            break
        elif (mulligan == "Yes" or mulligan == "yes" or mulligan == "y" or mulligan == "Y"):
            randnum = Mulligan(maxclue)
            print ("Your clue is " + str(filename[randnum]))
            print ("You have " + str(maxmulligan-mull) + " remaining")
            mull+=1
        elif (mulligan == "No" or mulligan == "no" or mulligan == "n" or mulligan == "N"):
            break
        else:
            print("Invalid input. Try again.")
    
    peek =  input("The correct number is " + str(correctnum))
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print ("Your clue is " + str(filename[randnum]))
    while (True):
        try:
            Guess = int(input("Guess a number between 0-100: "))
            break
        except ValueError:
            print ("Invalid input. Try again.")
    print ("The correct number is " + str(correctnum))
    mull = 0
    return Guess

#Calculating another random number for clue
def Mulligan(maxclue):
    clue = random.randrange(5,maxclue)
    return clue
           
#Calculating score after guess
def Calculate(guessnum,correctnum,team):
    if (guessnum > correctnum and guessnum <= correctnum + 2) and (guessnum < correctnum and guessnum >= correctnum - 2) or guessnum == correctnum:
        print ("Team " + str(team+1) + " has gained 4 points!")
        return 4
    elif (guessnum > correctnum and guessnum <= correctnum+4) or (guessnum < correctnum and guessnum >= correctnum - 4):
        print ("Team " + str(team+1) + " has gained 3 points!")
        return 3
    elif (guessnum > correctnum  and guessnum <=correctnum+6) or (guessnum < correctnum and guessnum >= correctnum - 6):
        print ("Team " + str(team+1) + " has gained 2 points!")
        return 2
    else:
        print ("Team " + str(team+1) + " has gained 0 points.")
        return 0

#Calculate and print out scoreboard
def Score(teampoints,currentteam,points):
    teampoints[currentteam] = teampoints[currentteam] + points
    for i in range(len(teampoints)-1):
        print ("Team " + str(i+1) + ": " + str(teampoints[i]))

#Determine how many points needed to win the game

def main():
    #setting up game
    guessrange = random.randrange(0,100)
    currentteam = 0
    cluelist = open("telewaveclues.txt","r")
    content = cluelist.readlines()
    numteams = int(content[1])
    maxmulligan = int(content[3])
    end = int(content[5])
    maxclue = file_len("telewaveclues.txt")                     
    #Starting game 
    teampoints = [0 for i in range(numteams+1)]
    print ("There are " + str(numteams) + " teams.")
    print ("You must get " + str(end) + " points to win.")
    print ("There are " + str(maxmulligan) + " mulligans you have each round.")
    while (True):
        try:
            guessrange = random.randrange(0,100)
            clue = random.randrange(2,maxclue)
            guess = Play(content,clue,guessrange,currentteam,maxclue,maxmulligan)
            points = Calculate(guess,guessrange,currentteam)
            Score(teampoints,currentteam,points)
            if (teampoints[currentteam] == int(end) or teampoints[currentteam] >= int(end)):
                print ("Team " + str(currentteam+1) + " has won the game!")
                break
            currentteam +=1
            if (currentteam == numteams):
                currentteam = 0
        except KeyboardInterrupt:
            print ("The game has ended.")
            Score(teampoints,currentteam,0)
            end = input()
            break
    
main()
