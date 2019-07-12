#!/usr/local/bin/python

"""
Game Of Greed
"""

import random
import time

# initialized values
max_turns = 3
min_dice_val = 1
max_dice_val = 6

def welcome():
    print("Welcome to Game of Greed\n")
    time.sleep(.3)

def start_turn():
    current_turn = 0
    money_pot = 0
    bank = 0

    while current_turn < max_turns:
        num_dice_to_roll = 6

        while num_dice_to_roll > 0:
            print('\n***********************')
            print(f'BANK VALUE: {bank}')
            print(f'MONEY POT VALUE: {money_pot}')
            print(f'CURRENT TURN: {current_turn}.')
            print('***********************\n')

            time.sleep(.3)
            print("rolling dice...\n")
            time.sleep(.3)

            # go to do_round function
            num_dice_to_roll, money_pot, bank, current_turn = do_round(num_dice_to_roll, money_pot, bank, current_turn)
        

        if num_dice_to_roll == 0:
            # user_input_to_bank = input("Out of dice. Enter b to bank: ")
           
            print('Points banked and dice reset.\n')

            money_pot, bank = bank_round(money_pot, bank)

    current_turn += 1
    print("Out of turns.\n")
    print(f'You scored {bank} points!')
    quit()


def do_round(num_dice_to_roll, money_pot, bank, current_turn):
    dice_rolled = []

    for i in range(num_dice_to_roll):
       dice_rolled.append(random.randint(min_dice_val, max_dice_val))
    print(f'You rolled: {dice_rolled}\n')   
    user_selection = str(input("Enter dice to keep or enter 'b' to bank: "))
    
    # Go to make_choice function
    user_selection, bank, money_pot = make_choice(user_selection, bank, money_pot)

    if user_selection == 'b':
        current_turn += 1
        money_pot = 0
        num_dice_to_roll = 0
        return num_dice_to_roll, money_pot, bank, current_turn
    
    user_selection = [char for char in user_selection]
    num_dice_to_roll -= len(user_selection)
    return num_dice_to_roll, money_pot, bank, current_turn

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