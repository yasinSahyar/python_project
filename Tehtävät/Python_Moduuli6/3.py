##
def convert_to_litres(gallons):
    litres = gallons * 3.78541
    return litres

while True:
    gallons = float(input("Enter the quantity of gasoline in American gallons (negative value to exit): "))
    if gallons < 0:
        break          ##user inputs a negative value, the loop breaks and the program ends.
    litres = convert_to_litres(gallons)
    print(f"{gallons} gallons is equal to {litres:.2f} litres.")



"""
Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
Write a main program that asks for a volume in gallons from the user and converts the value to liters.
The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
"""

"""
2.function takes a single argument, gallons, which is the quantity of gasoline in American gallons that we want to convert to litres
10.Inside the loop, the program reads the user’s input as a float and stores it in the gallons variable


"""