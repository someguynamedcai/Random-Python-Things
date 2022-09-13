import os
import random

TITLE_IMAGE = '''
___________    .__                                     
\__    ___/___ |  |   ______  _  _______ ___  __ ____  
  |    |_/ __ \|  | _/ __ \ \/ \/ /\__  \\  \/ // __ \ 
  |    |\  ___/|  |_\  ___/\     /  / __ \\   /\  ___/ 
  |____| \___  >____/\___  >\/\_/  (____  /\_/  \___  >
             \/          \/             \/          \/ 
'''

MAIN_MENU = '''[1] Play Game [2] Add Clues [3] Quit\n'''

DEFAULT_TEAM_NAMES = ["Team Amazing","Team Brilliant","Team Champions", "Team Deft", "Team Elevated", "Team Favorites", "Team Greatness", "Team Hopeful", "Team Invincible", "Team Jovial", "Team Knowledgeable", "Team Lasers"]

def clear():
    os.system('cls')

def parse_clues():
    with open("Telewave/telewaveclues.txt") as f:
        clues = f.readlines()
    return clues

#Allows adding more clues
def add_clues():
    adding_clues = True
    user_input = ''
    while (adding_clues):
        new_clue = input("Type the clue that you want to add to the list with a comma in between. \nExample: Cold,Hot: ")
        while user_input not in ["1","2"]:
            print("The clue you want to add is:\n" + new_clue)
            user_input = input("[1] Confirm and Add Clue [2] Cancel\n")    
            if user_input not in ["1","2"]:
                print("Invalid input.\n")

        if user_input == '1':
            with open("Telewave/telewaveclues.txt","a") as f:
                f.write("\n" + new_clue)
                print("Clue added successfully!")

        elif user_input == '2':
            return
        
        user_input = ''
        while user_input not in ["1","2"]:
            user_input = input("Do you want to add more clues? \n[1] Yes [2] No\n")
            if user_input not in ["1","2"]:
                print("Invalid input.\n")
        if user_input == "1":
            adding_clues = True
        if user_input == "2":
            adding_clues = False
        
#Choose how many teams are playing
def set_teams():
    team_count = ''
    while isinstance(team_count, int) == False:
        try:
            team_count = int(input("How many teams do you want to have (e.g. 2, 5)? "))
            if (team_count <=1):
                print ("You cannot have less than 2 teams. Please add more teams.")
        except ValueError:
            print ("Invalid input. Try again.")
            continue
    team_names = {}
    for team in range(team_count):
        user_input = input(f"Enter a name for team {team} or leave blank to accept default '{DEFAULT_TEAM_NAMES[team]}':\n")
        if user_input == "":
            team_names.update({DEFAULT_TEAM_NAMES[team]: 0})    
        else:
            team_names.update({user_input: 0})
    return team_names
    
def print_scores(teams):
    print("Current Scores:")
    print(teams)

def get_clue():
    clue_list = parse_clues()
    return random.choice(clue_list)

def get_correct_answer():
    return random.randrange(0,100)

#Playing a round
def play_round(teams):
    for team in teams.keys():
        print_scores(teams)
        print(f"{team} is up!")
        clue_confirmed = False
        while clue_confirmed == False:
            clue = get_clue()
            print(clue)
            user_input = ""
            while user_input not in ["1","2"]:
                user_input = input("[1] Accept Clue [2] Get Another Clue\n")
            if user_input == "1":
                clue_confirmed = True
        correct_answer = get_correct_answer()
        input(f"Correct answer is {correct_answer}. Press enter to hide the correct answer and present clue.")
        clear()
        print_scores(teams)
        print("Scoring: +-2 = 4 points, +-4 = 3 points, +-6 = 2 points, otherwise 0 points.")
        print(clue)
        guess = ''
        while isinstance(guess, int) == False:
            try:
                guess = int(input("Guess a number between 0 and 100: "))
            except ValueError:
                print ("Invalid input. Try again.")
                continue
        points_awarded = calculate_score(guess, correct_answer)
        
        print(f"{team} has gained {points_awarded} points.")
        teams.update({team: teams.get(team) + points_awarded})
           
#Calculating score after guess
def calculate_score(guess,correct_answer):
    deviation = abs(guess - correct_answer)
    if deviation <= 2:
        return 4
    elif deviation <= 4:
        return 3
    elif deviation <= 6:
        return 2
    else:
        return 0

#Determine how many points needed to win the game
def set_end_score():
    end_score = ''
    while isinstance(end_score, int) == False:
        try:
            end_score = int(input("How many points to win: "))
        except ValueError:
            print ("Invalid input. Try again.")
            continue
    return end_score

def main():
    game_is_active = True
    
    #Starting game 
    while game_is_active == True:
        
        print(TITLE_IMAGE)
        selection = input(MAIN_MENU)
        if selection == '2':
            add_clues()

        elif selection == '3':
            print("Thank you for playing!")
            game_is_active = False

        elif selection == '1':
            #setting up game variables
            teams = set_teams()
            end_score = set_end_score()
            round_number = 1

            while max(teams.values()) <= end_score:
                print(f"Round {round_number}")
                play_round(teams)
            print ("GAME OVER! Final scores:")
            print(teams)
    
main()
