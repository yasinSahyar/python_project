##
import math

def calculate_unit_price(diameter: float, price: float) -> float:
    radius = diameter / 2
    area = math.pi * radius ** 2
    unit_price = price / area * 10000
    return unit_price

diameter1 = float(input("Enter the diameter of the first pizza in centimeters: "))
price1 = float(input("Enter the price of the first pizza in euros: "))
unit_price1 = calculate_unit_price(diameter1, price1)

diameter2 = float(input("Enter the diameter of the second pizza in centimeters: "))
price2 = float(input("Enter the price of the second pizza in euros: "))
unit_price2 = calculate_unit_price(diameter2, price2)

if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")




"""
Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
 The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to
 enter the diameter and price of two pizzas and tells the user which pizza provides better value for money
 (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.

"""

"""
4-8.The calculate_unit_price function takes two parameters: diameter and price. It first calculates the radius of the pizza 
by dividing the diameter by 2. It then calculates the area of the pizza using the formula π * radius^2. Finally, it calculates 
the unit price of the pizza per square meter by dividing the price by the area and multiplying by 10,000 to convert 
from square centimeters to square meters

10-20.In this example, the user is prompted to enter the diameter and price of two pizzas. The calculate_unit_price function is then
 called to calculate the unit price of each pizza per square meter. Finally, the program compares the unit prices of the two pizzas
  and tells the user which pizza provides better value for money.
"""