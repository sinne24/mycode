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
    try:
        print("\nWelcome, this will help you choose a pokemon starter!")
        element = int(input("Choose between these three elements: Fire, Water, Grass"))
        year = int(input("Type in a four digit number between 1990 and 2023"))
        print("You chose " + element + " and " + year)

        if element == 'Fire': 
            if year >= 1990 && year <= 2000:
                print("Your starter is Charmander")
            elif year >= 2001 && year <= 2010:
                print("Your starter is Cyndaquil")
            elif year >= 2011 && year <= 2020:
                print("Your starter is Torchic")
            else:
                print("Your starter is Fuecoco")
            break             # break statement escapes the while loop
        elif element == 'Water':    
            if year >= 1990 && year <= 2000:
                print("Your starter is Squirtle")
            elif year >= 2001 && year <= 2010:
                print("Your starter is Totodile")
            elif year >= 2011 && year <= 2020:
                print("Your starter is Mudkip")
            else:
                print("Your starter is Quaxly")
            break             # break statement escapes the while loop
        elif element == 'Grass':    
            if year >= 1990 && year <= 2000:
                print("Your starter is Bulbasaur")
            elif year >= 2001 && year <= 2010:
                print("Your starter is Chikorita")
            elif year >= 2011 && year <= 2020:
                print("Your starter is Treeko")
            else:
                print("Your starter is Sprigatito")
            break             # break statement escapes the while loop
        else:
            print('Invalid element entered')

        # general error handling
        # a practical use might be exceptions we haven't designed solution for yet
        except Exception as err:
            # sys.exc_info returns a 3 tuple with into about the exception handled
            print("We did not anticipate that:", err)
            # raise by itself simply calls the previous exception that was thrown
            raise


