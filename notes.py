#!/usr/local/bin/python

"""
Game Of Greed
"""

def welcome():
    print("Welcome to Game of Greed.")

    round = 1
    total_score = 0

    while round <= 10:
        
        round_score = do_round()
        total_score += round_score
        print("tot: ", total_score, "round: ", round)
        round += 1
    
    print("Adios ", total_score)
        
def do_round():
    round_score = 0

    while True:
        response = input("Enter response: \n")
        print("Your response:", response)
        if response == 'r':
            # roll dice
            # select dice
            # enter round score
            return 
        if response == 'b':
            return round_score
        
        if response == 'z':
            return 0

        round_score += 5

welcome()

--------------

def make_choice():
    print("made choice")

def enter_score(score_this_round):
    enter_points = int(input("Enter score for last round: "))
    score_this_round += enter_points
    return score_this_round


def prompt_after_roll():
    print("""
    Options: 
    Enter at least one dice number to roll again.
    Enter 'b' to bank points.
            """)

def selection_after_prompt():
    player_selection = str(input()).lower()
    print("player_selection:", player_selection)

    if player_selection == '#######': #The dice numbers
        for i in player_selection.split():
            dice_kept_this_round.append(i) 

    elif player_selection == 'b':
        #calculate the score_this_round
        # global overall_score += score_this_round
        print('TBD')

    elif player_selection == 'r':
        #remove the num of dice selected
        #roll the num of dice remaining
        print('TBD')
        
    elif player_selection == 'q':
        print('Thank you for playing. Goodbye.')
        exit()

    else:
        print("Not a valid selection. Please try again.")
        # This requires a while loop

    return player_selection

def bank_points():
    pass