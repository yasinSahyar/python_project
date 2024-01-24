##

numbers = []

while True: ##无限循环
    user_input = input("Enter a number (Enter an empty string to quit): ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if len(numbers) > 0:
    smallest_number = min(numbers)
    largest_number = max(numbers)

    print("Smallest number:", smallest_number)
    print("Largest number:", largest_number)
else:
    print("No numbers entered.")



"""
Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
"""

"""
 3.The variable numbers is initialized as an empty list. This list will be used to store the numbers entered by the user.
 
 11.Inside the loop, the program attempts to convert the user's input to a floating-point number using float(user_input).
 
 13.he number is added to the numbers list using numbers.append(number).
 
 18.If numbers were entered, it calculates the smallest and largest numbers using min(numbers) and max(numbers), respectively.
 
 


"""