import random 

#check how many lines are in clue list 
def file_len(filename):
    with open(filename) as f:
        for i, _ in enumerate(f):
            pass
    return i + 1

#Allows adding for more clues
def Addclues(addlist):
    while (True):
        Addclue = input("Do you want to add more clues? ")
        if (Addclue == "No" or Addclue == "no" or Addclue == "n" or Addclue == "N"):
            addlist.close()
            break;
        elif (Addclue == "Yes" or Addclue == "yes" or Addclue == "y" or Addclue == "Y"):
            Newclue = input("Type the clues that you want to add to the list with a comma in between. \nExample: ClueA,ClueB: ")
            Final = input("Are you sure these are the clues you want to add? ")
            if (Final == "Yes" or Final == "Y" or Final == "y" or Final == "yes"):
                addlist.write("\n" + Newclue)
                print ("Added " + str(Newclue) + " to the clue list.")
            else:
                print ("Resetting.")
        else:
            print ("Invalid input. Try again.")
        
#Choose how many teams are playing
def Chooseteams():
    while (True):
        try:
            numteams = int(input("How many teams do you want to have? "))
            if (numteams <=1):
                print ("You cannot have less than 2 teams. Please add more teams.")
            else:
                break;
        except ValueError:
            print ("Invalid input. Try again.")
    return numteams
    
#Playing the game
def play(filename,randnum,correctnum,currentteam):
    print ("Team " + str(currentteam+1) + " is up.")
    print ("Your clue is " + str(filename[randnum]))
    while (True):
        mulligan = input("Do you want another clue? ")
        if (mulligan == "Yes" or mulligan == "yes" or mulligan == "y" or mulligan == "Y"):
            randnum = Mulligan(clue,maxclue)
            print ("Your clue is " + str(filename[randnum]))
        else:
            break
    peek =  input("The correct number is " + str(correctnum))
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    while (True):
        try:
            Guess = int(input("What number would you like to guess? "))
        except ValueError:
            print ("Invalid input. Try again.")
        break;
    print ("The correct number is " + str(correctnum))
    return Guess

#Calculating another random number for clue
def Mulligan(clue,maxclue):
    clue = random.randrange(maxclue)
    return clue
           
#Calculating score after guess
def Calculate(guessnum,correctnum,team):
    print ((guessnum > (correctnum + 4)))
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
def End():
    while (True):
        try:
            endscore = input("How many points to win: ")
        except ValueError:
                print ("Invalid input. Try again.")
        break
    return endscore

def main():
    #setting up game
    guessrange = random.randrange(0,100)
    addlist = open("telewaveclues.txt", "a")
    currentteam = 0
    cluelist = open("telewaveclues.txt","r")
    content = cluelist.readlines()
    maxclue = file_len("telewaveclues.txt")

    #Starting game 
    Addclues(addlist)
    numteams = Chooseteams()
    end = End()
    teampoints = [0 for i in range(numteams+1)]
    while (True):
        try:
            guessrange = random.randrange(0,100)
            clue = random.randrange(maxclue)
            Guess = play(content,clue,guessrange,currentteam)
            points = Calculate(Guess,guessrange,currentteam)
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
