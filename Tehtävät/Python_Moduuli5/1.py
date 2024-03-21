##
import random

# Prompt the user to enter the number of dice to roll
num_dice = int(input("How many dice would you like to roll? "))


dice_sum = 0                                                              # Initialize a variable to keep track of the sum of the dice rolls


for i in range(num_dice):                                                # The for loop iterates num_dice times.
    roll = random.randint(1, 6)                                    #
    dice_sum += roll


print(f"The sum of the {num_dice} dice rolls is {dice_sum}.")            #打印结果








"""
1.Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints
 out the sum of the numbers. Use a for loop.
 
11. The for loop iterates num_dice times.
    Inside the loop, random.randint(1, 6) generates a random integer between 1 and 6 (inclusive), simulating a six-sided die roll.
    The result of each die roll is added to the dice_sum variable.

"""




"""
2.This line imports the random module, which provides functions for generating random numbers.
In this code, it's used to simulate dice rolls.



"""