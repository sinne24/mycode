#!/usr/bin/python3
"""Lab 48 Mini Project: IF-LOGIC SCRIPT"""

def main():
    """runtime"""
    # code goes here

    # step 1. COMMENTS FIRST

    # step 2- Code what you know
    
    # step 3 - research what you don't
    
    # step 4 - test

    # step 5 - clean it up!

# Start with an infinite loop
while True:
        print("\nWelcome, this will help you choose a pokemon starter!")
        element = input("Choose between these three elements: Fire, Water, Grass: ")
        year = int(input("Type in a four digit number between 1990 and 2023: "))
        print("You chose " + element + " and " + str(year))

        if element == 'Fire': 
            if year >= 1990 and year <= 2000:
                print("\nYour starter is Charmander")
            elif year >= 2001 and year <= 2010:
                print("\nYour starter is Cyndaquil")
            elif year >= 2011 and year <= 2020:
                print("\nYour starter is Torchic")
            else:
                print("\nYour starter is Fuecoco")
            break             # break statement escapes the while loop
        elif element == 'Water':    
            if year >= 1990 and year <= 2000:
                print("Your starter is Squirtle")
            elif year >= 2001 and year <= 2010:
                print("Your starter is Totodile")
            elif year >= 2011 and year <= 2020:
                print("Your starter is Mudkip")
            else:
                print("Your starter is Quaxly")
            break             # break statement escapes the while loop
        elif element == 'Grass':    
            if year >= 1990 and year <= 2000:
                print("Your starter is Bulbasaur")
            elif year >= 2001 and year <= 2010:
                print("Your starter is Chikorita")
            elif year >= 2011 and year <= 2020:
                print("Your starter is Treeko")
            else:
                print("Your starter is Sprigatito")
            break             # break statement escapes the while loop
        else:
            print('Invalid element entered')

