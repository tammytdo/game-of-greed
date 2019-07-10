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