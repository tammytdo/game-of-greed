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
        # Current turn
        print(f'You are on turn {current_turn}.\n')
        num_dice_to_roll = 6

        while num_dice_to_roll > 0:
            time.sleep(.3)
            print("rolling dice...\n")
            time.sleep(.3)

            # do_round function
            num_dice_to_roll, money_pot, bank = do_round(num_dice_to_roll, money_pot, bank)

        current_turn += 1
        print("Out of turns.")
        print(f'You scored {bank} points!')
        quit()


def do_round(num_dice_to_roll, money_pot, bank):
    dice_rolled = []

    for i in range(num_dice_to_roll):
       dice_rolled.append(random.randint(min_dice_val, max_dice_val))
    print(f'You rolled: {dice_rolled}\n')   
    user_selection = str(input("Enter dice to keep or enter 'b' to bank: "))

    # do_round functions
    user_selection, bank, money_pot = make_choice(user_selection, bank, money_pot)
    user_selection = [char for char in user_selection]
    num_dice_to_roll -= len(user_selection)
    return num_dice_to_roll, money_pot, bank

def make_choice(user_selection, bank, money_pot):
    if user_selection == 'b':
        print("inside make_choice. bank + money_pot = ", bank, money_pot)
        bank += money_pot
        return bank
    else:
        point_value = int(input("Enter points for this roll: "))
        point_value += money_pot
        print("inside make_choice. point_value + money_pot = ", point_value, money_pot)

        return user_selection, bank, money_pot

# def bank_round(money_pot, bank):
#     bank += money_pot
#     print("in bank_round()")

def main():
    welcome()
    start_turn()

main()