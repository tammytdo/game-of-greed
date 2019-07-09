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

point_guide = {
    '5': 50,
    '1': 100
}

actions_dict = {'b': 'Bank Points',
           'r': 'Roll Dice',
           'q': 'Quit Game'
          }

for i in range(num_dice):
    dice_rolled.append(random.randint(min, max))

action_selection = """
Options: 
Enter at least one dice number to roll again.
Enter 'b' to bank points.
Enter 'q' to quit the game:
            """

print('Random dice rolled: ', dice_rolled)
# print(f'Random dice rolled: {dice_rolled}')
# why doesn't this f string work?

def prompt_after_roll():
    print(action_selection)

def selection_after_prompt():
    player_selection = str(input()).lower()

    # if player_selection == THE DICE NUMBERS:
        for i in player_selection.split():
            dice_kept_this_round.append(i):
            

    elif player_selection == 'b':
        #calculate the score_this_round
        # overall_score += score_this_round
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

#Fuction Calls
prompt_after_roll()
selection_after_prompt()






"""
Add to points_guide once I understand how to calculate:

    #'three of a kind': 100 * times the number rolled,
    #'except for three ones': 1000,
    #'four, five, or six of a kind': each additional die is worth double the three of a kind score
        # This makes the highest possible score in a single roll 4000 for six ones (1000 for three ones, after that player gains 1000 points for each additional one in that series of rolling.) The ONE is the only die you ever count in the thousands.
    #'A straight from 1 to 6': 1500
        # If a player fails to roll a straight they may make one attempt to complete the straight. If the desired number(s) does not turn up on the next roll that round is a "crap out" even if there are scoring dice on the table i.e. 1's or 5's.
    #'Three pairs': 1000 
        # For instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise (some places have their own house rules).
        # If a player fails to roll a three of a kind, they may make one attempt to complete the three of a kind. If the desired number(s) does not turn up on the next roll, that round is a "crap out", even if there are scoring dice on the table; i.e. 1's or 5's.
"""