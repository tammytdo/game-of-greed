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
            game_summary(bank, money_pot, current_turn, max_turns)

            rolling_die_text()

            num_die_to_roll, money_pot, bank, current_turn = do_round(num_die_to_roll, money_pot, bank, current_turn)
        
        if num_die_to_roll == 0:
            money_pot, bank, current_turn = bank_and_reset_die(money_pot, bank, current_turn)

    end_game(bank)

def do_round(num_die_to_roll, money_pot, bank, current_turn):
    die_rolled = []

    die_rolled, num_die_to_roll = determine_which_die_rolled(die_rolled, num_die_to_roll)

    # handle error for entries that are not a number or the letter b
    user_selection = str(input("Enter at least one die to roll again, or enter 'b' to bank points: "))
    
    #find out if zilch, single, double, triple., etc.
    
    user_selection, bank, money_pot = make_choice(user_selection, bank, money_pot)

    if user_selection == 'b':
        money_pot = 0   #reset money_pot
        num_die_to_roll = 0  #reset num_die_to_roll
        return num_die_to_roll, money_pot, bank, current_turn 

    user_selection = validate_user_input(user_selection)

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
        # Validate that input is an integer before adding to money_pot
        money_pot += points_earned_this_round

        return user_selection, bank, money_pot

def validate_user_input(user_selection):
    #Fix to allow user to also enter with spaces 
    user_selection = [int(char) for char in user_selection]
    return user_selection

def game_summary(bank, money_pot, current_turn, max_turns):
    print('\n***********************')
    print(f'BANK VALUE        {bank}')
    print(f'MONEY POT VALUE   {money_pot}')
    print(f'CURRENT TURN      {current_turn}/{max_turns}.')
    print('***********************\n')
    time.sleep(.3)

def rolling_die_text():
    print("rolling die...\n")
    time.sleep(.3)

def determine_which_die_rolled(die_rolled, num_die_to_roll):
    for i in range(num_die_to_roll):
        die_rolled.append(random.randint(min_die_val, max_die_val))
    
    print(f'You rolled: {die_rolled}\n')
    return die_rolled, num_die_to_roll

def bank_and_reset_die(money_pot, bank, current_turn):
    print('All die used\n')
    print('Points banked and die reset\n')

    time.sleep(.5)
    current_turn += 1
    print('New turn started\n')
    
    return money_pot, bank, current_turn

def bank_round(money_pot, bank, current_turn):
    bank += money_pot
    money_pot = 0
    return money_pot, bank 

def end_game(bank):
    print("Out of turns.\n")
    print(f'Game over. You scored {bank} points!')
    quit()

def main():
    welcome()
    start_turn()

main()