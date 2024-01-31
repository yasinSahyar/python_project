##
def get_season(month: int) -> str:
    seasons = ('winter', 'spring', 'summer', 'autumn')
    if month in (12, 1, 2):
        return seasons[0]
    elif month in (3, 4, 5):
        return seasons[1]
    elif month in (6, 7, 8):
        return seasons[2]
    else:
        return seasons[3]

month = int(input("Enter a month number: "))
season = get_season(month)
print(f"The season corresponding to month {month} is {season}.")

"""
Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter).
 Save the seasons as strings into a tuple in your program. We can define each season to last three months,December being the first month of winter.
"""

"""
2.function named get_season that takes an integer parameter month and returns a string
2.(-> int and -> str) indicate that the function returns a string.
3.A tuple named seasons is defined
4.if else --statements to determine the season based on the input month.
14.The code prompts the user to enter a month number, converts the input to an integer, and stores it in the variable month.

"""