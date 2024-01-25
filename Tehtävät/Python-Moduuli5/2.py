##

numbers = []
while True:                                                              #无限循环infin
    num = input("Enter a number (or an empty string to quit): ")
    if num == "":                                                       #empty string, the loop is terminated
        break
    numbers.append(float(num))                          #the entered value is converted to a float using float(num) and added to the numbers list.

numbers.sort(reverse=True)
print(f"The five greatest numbers are: {numbers[:5]}")


"""
2.Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, 
the program prints out the five greatest numbers sorted in descending order. 
Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
"""

"""
line
3.This line creates an empty list called numbers that will be used to store the numbers entered by the user.

8.Otherwise, the entered value is converted to a float using float(num) and added to the numbers list.

10.After the user exits the loop, the program sorts the numbers list in descending order using the sort method with reverse=True

"""