##
import math

while True:
    num = input("Enter an integer (or an empty string to quit): ")
    if num == "":
        break
    num = int(num)
    is_prime = True

    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


"""

3.Write a program that asks the user for an integer and tells if the number is a prime number.
 Prime numbers are number that are only divisible by one or the number itself.

For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
"""

"""
4.The program enters an infinite loop (while True) to repeatedly prompt the user to enter an integer.

7.If the user enters an empty string , the loop is terminated with the break statement.
Otherwise, the entered value is converted to an integer using int(num).

14. If the number is greater than 1, the program checks for divisibility by any integer from 2 to the
   square root of the number (inclusive). If it is divisible, is_prime is set to False, and the loop is terminated with break
   
   
"""