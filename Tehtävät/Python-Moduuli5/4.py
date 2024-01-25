##
cities = []                                                                         # Initialize an empty list to store city names


for i in range(5):                                                                      #loop to iterate five times.
    city_name = input(f"Enter the name of city {i + 1}: ")
    cities.append(city_name)


print("List of cities:")                                                        #loop to iterate through the list and print city names
for city in cities:
    print(city)

"""
Write a program that asks the user to enter the names of five cities one by on (use a for loop for 
reading the names) and stores them into a list structure. Finally, the program prints out the names of 
the cities one by one,  one city per line, in the same order they were read as input. 
Use a for loop for asking the names and a for/in loop to iterate through the list.
"""

"""
2.This line initializes an empty list called cities to store the names of the cities.

5.6. The program uses a for loop to iterate five times.
    Inside the loop, the user is prompted to enter the name of each city using input.
    The entered city name is then appended to the cities list.
    
10.After collecting all the city names, the program uses a for/in loop to iterate through the cities list.
"""
