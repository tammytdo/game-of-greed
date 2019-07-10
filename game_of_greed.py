#!/usr/local/bin/python

"""
Game Of Greed
"""

import random

min = 1
max = 6
overall_score = 0
score_this_round = 0
num_dice = 6
dice_rolled = []
dice_kept_this_round = []
round = 1

def welcome():
    return "Welcome to Game of Greed."

def rolling_dice():
    return "\nrolling dice..."

def dice_roll_results():
    for i in range(num_dice):
       dice_rolled.append(random.randint(min, max))
    
    print('You rolled: ', dice_rolled)
    
    response = input('Would you like to keep any dice? Y or N ').lower()

    while True: 
        if response == "y":
            user_keeping_these_dice = input("Which would you like to keep? ").split()

            for i in user_keeping_these_dice:
                print("I: ", i)
                dice_rolled.append(dice_kept_this_round)


            print("dice_kept_this_round", dice_kept_this_round)

        if response == "n":
            return False

        else:
            print('Please enter Y or N.')

    print('exited')

# def enter_score(score_this_round):
#     enter_points = int(input("Enter score for last round: "))
#     score_this_round += enter_points
#     print(score_this_round)



# def prompt_after_roll():
#     print("""
# Enter a response: 
#   'R' to roll again.
#   'B' to bank points.
#   'Q' to quit the game:
#             """)

#     # while response not 'Q': 
#     #     if response 'R':
#     #     if response 'R':
#     #     if response 'R':
            
# def selection_after_prompt():
#     player_selection = str(input()).lower()

#     if player_selection == 'THE DICE NUMBERS':
#         for i in player_selection.split():
#             dice_kept_this_round.append(i)
            

#     elif player_selection == 'b':
#         #calculate the score_this_round
#         # overall_score += score_this_round
#         print('TBD')

#     elif player_selection == 'r':
#         #remove the num of dice selected
#         #roll the num of dice remaining
#         print('TBD')
        
#     elif player_selection == 'q':
#         print('Thank you for playing. Goodbye.')
#         exit()

#     else:
#         print("Not a valid selection. Please try again.")
#         # This requires a while loop

#     return player_selection

#Fuction Calls
print(welcome())
print(rolling_dice())
dice_roll_results()


# enter_score(score_this_round)

# prompt_after_roll()
# selection_after_prompt()

