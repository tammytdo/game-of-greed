#!/usr/local/bin/python

"""
Game Of Greed
"""

import random
import time

# initialized values
max_turns = 3
min_die_val = 1
max_die_val = 6

#BUG GAME TURNS ARE DOUBLE INCREMENTING WHEN BANKING AND WHEN NUM DICE TO ROLL = 0.

def welcome():
    print("Welcome to Game of Greed")
    time.sleep(.3)

def start_turn():
    current_turn = 1
    money_pot = 0
    bank = 0

    while current_turn < max_turns + 1:
        num_die_to_roll = 6

        while num_die_to_roll > 0:
            print('\n***********************')
            print(f'BANK VALUE        {bank}')
            print(f'MONEY POT VALUE   {money_pot}')
            print(f'CURRENT TURN      {current_turn}/{max_turns}.')
            print('***********************\n')

            time.sleep(.3)
            print("rolling die...\n")
            time.sleep(.3)

            # go to do_round function
            num_die_to_roll, money_pot, bank, current_turn = do_round(num_die_to_roll, money_pot, bank, current_turn)
        
        if num_die_to_roll == 0:
            # user_input_to_bank = input("Out of die. Enter b to bank: ")

            print('All die used\n')
            print('Points banked and die reset\n')

            time.sleep(.5)
            current_turn += 1
            print('New turn started\n')
            
            money_pot, bank = bank_round(money_pot, bank)

    print("Out of turns.\n")
    print(f'You scored {bank} points!')
    quit()


def do_round(num_die_to_roll, money_pot, bank, current_turn):
    die_rolled = []

    for i in range(num_die_to_roll):
       die_rolled.append(random.randint(min_die_val, max_die_val))
    
    print(f'You rolled: {die_rolled}\n')   
    user_selection = str(input("Enter at least one die to roll again, or enter 'b' to bank points: "))
    
    #check if each number in input.split() is in die_rolled.
    #if in die_rolled, use index() of the input to find it's index in die_rolled. pop the num at that index out. add it to a new array. find out if zilch, single, double, triple., etc.
    
    # Go to make_choice function
    user_selection, bank, money_pot = make_choice(user_selection, bank, money_pot)

    if user_selection == 'b':
        current_turn += 1
        money_pot = 0
        num_die_to_roll = 0
        return num_die_to_roll, money_pot, bank, current_turn
    
    user_selection = [int(char) for char in user_selection]
    
    user_selection, die_rolled = remove_from_die_rolled(user_selection, die_rolled)
    
    num_die_to_roll -= len(user_selection)
    return num_die_to_roll, money_pot, bank, current_turn

def remove_from_die_rolled(user_selection, die_rolled):
    for i in user_selection:
        # keep for debugging elif statement
        # print("i is", i, "and type is", type(i))

        if i in user_selection:
            die_rolled.remove(i)
            print(f'Dice #{i} kept')

        # Why won't this message print when the dice value i is not present in user_selection?  
        elif i not in die_rolled:
            print('Invalid die selection.')

    return user_selection, die_rolled

def make_choice(user_selection, bank, money_pot):
    
    if user_selection == 'b':
        bank += money_pot
        return user_selection, bank, money_pot

    else:
        points_earned_this_round = int(input("\nHow many points for this roll? "))
        money_pot += points_earned_this_round

        return user_selection, bank, money_pot

def bank_round(money_pot, bank):
    bank += money_pot
    money_pot = 0
    return money_pot, bank 

def main():
    welcome()
    start_turn()

main()