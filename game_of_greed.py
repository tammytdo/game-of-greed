#!/usr/local/bin/python

from house_rules import calculate_points
import random
import time

"""
Game Of Greed
"""

# initialized values
max_turns = 3
min_die_val = 1
max_die_val = 6

# Game play 
def welcome():
    print("Welcome to Game of Greed")
    time.sleep(.3)

    start_turn()

def start_turn():
    current_turn = 1
    money_pot = 0
    bank = 0

    while current_turn < max_turns + 1:
        num_die_to_roll = 6

        while num_die_to_roll > 0:
            # game_summary function
            game_summary(bank, money_pot, current_turn, max_turns)

            # rolling_die_text function
            rolling_die_text()

            # do_round function
            num_die_to_roll, money_pot, bank, current_turn = do_round(num_die_to_roll, money_pot, bank, current_turn)
        
        if num_die_to_roll == 0:
            # bank_and_reset_die function
            money_pot, bank, current_turn = bank_and_reset_die(money_pot, bank, current_turn)

    # end_game function
    end_game(bank)


# Game logic
def do_round(num_die_to_roll, money_pot, bank, current_turn):
    die_rolled = []
    die_kept = []
    # breakpoint() 
    die_rolled, num_die_to_roll = die_roll_results(die_rolled, num_die_to_roll)        

    # handle error for entries that are not a number or the letter b
    user_selection = str(input("Enter at least one die to roll again, or enter 'b' to bank points: "))
        
    user_selection, bank, money_pot, die_kept = make_choice(user_selection, bank, money_pot, die_kept)

    if user_selection == 'b':
        money_pot = 0   #reset money_pot
        num_die_to_roll = 0  #reset num_die_to_roll
        return num_die_to_roll, money_pot, bank, current_turn 

    user_selection = user_selection_to_string(user_selection)

    user_selection, die_rolled, die_kept = remove_from_die_rolled(user_selection, die_rolled, die_kept)
    
    num_die_to_roll -= len(user_selection)
    return num_die_to_roll, money_pot, bank, current_turn

def remove_from_die_rolled(user_selection, die_rolled, die_kept):

    for i in user_selection:
        # keep for debugging elif statement
        # print("i is", i, "and type is", type(i))

        if i in user_selection:
            die_rolled.remove(i)
            die_kept.append(i)
            print(f'Dice #{i} kept')

        # Why won't this message print when the dice value i is not present in user_selection?  
        elif i not in die_rolled:
            print('Invalid die selection.')

    return user_selection, die_rolled, die_kept

def make_choice(user_selection, bank, money_pot, die_kept):
    
    if user_selection == 'b':
        bank += money_pot
        return user_selection, bank, money_pot, die_kept

    else:
        for i in user_selection:
            die_kept.append(i)
            
        points_earned = calculate_points(die_kept)
        money_pot += points_earned 

        return user_selection, bank, money_pot, die_kept

def user_selection_to_string(user_selection):
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

def die_roll_results(die_rolled, num_die_to_roll):
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

if __name__ == "__main__":
    welcome()