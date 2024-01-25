##Tehtävä2

import math

def calculate_area(radius):
    return math.pi * radius**2

## Ask radius
radius = float(input("Enter the radius of the circle: "))

## Calculate the area
area = calculate_area(radius)

## Print
print(f"The area of the circle with radius {radius} is {area:.2f} square units.")