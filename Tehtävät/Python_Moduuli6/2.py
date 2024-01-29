##
import random

def roll_dice(num_sides):
    return random.randint(1, num_sides)

def main():
    num_sides = int(input("Enter the number of sides on the dice: "))

    result = 0                                                          ##initializes the result variable to 0.
    rolls = 0                                                           ##                 rolls

    while result != num_sides:
        result = roll_dice(num_sides)
        rolls += 1
        print(f"Roll {rolls}: {result}")

    print(f"Congratulations! It took {rolls} rolls to get the maximum number on the {num_sides}-sided dice.")

main()

"""
Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function 
you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling 
in the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.
"""

"""
4.It uses random.randint(1, num_sides) to generate a random integer between 1 and num_sides, inclusive, representing the result of a roll.
13.while loop continues until result is equal to num_sides, meaning the maximum number on the dice entered by the user.


"""
