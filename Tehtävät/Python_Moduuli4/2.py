###

while True: ##程序进入无限循环

    inches = float(input("Enter the length in inches (enter a negative value to end): "))

    # Check if the user wants to end the program
    if inches < 0:
        print("Program ended.")
        break

    # Convert inches to centimeters (1 inch = 2.54 centimeters)
    centimeters = inches * 2.54

    #  result
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters")





    """
    Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
    """

    """
    3.This line starts an infinite loop using while True(程序进入无限循环). This loop will continue indefinitely until it is explicitly broken out of using the break statement.
    
    5.Inside the loop, the program prompts the user to enter the length in inches using the input function. 
    
    16.f-string ,2f display only two decimal places.
    """

