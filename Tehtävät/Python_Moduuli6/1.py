##

import random

def roll_dice():
    return random.randint(1, 6)

def main():
    result = 0
    rolls = 0

    while result != 6:
        result = roll_dice()
        rolls += 1
        print(f"Roll {rolls}: {result}")

    print(f"Congratulations! It took {rolls} rolls to get a 6.")


main()



"""

Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
Write a main program that rolls the dice until the result is 6.  The main program should print out the result of each roll.
"""

"""
5.This function is defined to simulate rolling a six-sided die.
8.: This is the main function that orchestrates the simulation.
12. This is a while loop that continues until a 6 is rolled.


"""