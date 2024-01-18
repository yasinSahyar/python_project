##Tehtävä3

def calculate_perimeter(base, height):
    return 2 * (base + height)

def calculate_area(base, height):
    return base * height

## Ask base and height
base = float(input("Enter the base of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

## Calculate  perimeter and area
perimeter = calculate_perimeter(base, height)
area = calculate_area(base, height)

## results
print(f"The perimeter of the rectangle is {perimeter:.2f} units.")
print(f"The area of the rectangle is {area:.2f} square units.")