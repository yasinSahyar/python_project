##Tehtävä4


def calculate_sum(num1, num2, num3):
    return num1 + num2 + num3

def calculate_product(num1, num2, num3):
    return num1 * num2 * num3

def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

## Ask three integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

## Calculate sum, product, and average
sum_result = calculate_sum(num1, num2, num3)
product_result = calculate_product(num1, num2, num3)
average_result = calculate_average(num1, num2, num3)

## results
print(f"The sum of the numbers is {sum_result}.")
print(f"The product of the numbers is {product_result}.")
print(f"The average of the numbers is {average_result:.2f}.")