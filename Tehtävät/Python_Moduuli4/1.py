##

number = 1

while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1



"""
Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
"""




"""
3.Here, we initialize a variable number and set it to 1. This variable will be used to keep track of the current number being evaluated in the while loop.

5.This line starts a while loop that continues as long as the value of number is less than or equal to 1000.

6.Inside the while loop, we use an if statement to check if the current value of number is divisible by 3. The % operator is the modulo operator, which gives the remainder of the division. If the remainder is 0, it means that the number is divisible by 

6.If the condition in the if statement is true (i.e., the number is divisible by 3), we print the value of number.

8.Regardless of whether the if condition is true or false, we increment the value of number by 1 in each iteration of the loop. This ensures that we move on to the next number in the sequence.

"""