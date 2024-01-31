##
airports = {}
while True:                                                           ##无限循环infnt
    print("Enter 1 to enter a new airport")
    print("Enter 2 to fetch the information of an existing airport")
    print("Enter 3 to quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        icao_code = input("Enter the ICAO code of the airport: ")
        name = input("Enter the name of the airport: ")
        airports[icao_code] = name
        print(f"{name} has been added to the database.")
    elif choice == "2":
        icao_code = input("Enter the ICAO code of the airport: ")
        if icao_code in airports:
            print(f"The name of the airport is {airports[icao_code]}.")
        else:
            print("Airport not found in the database.")
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please try again.")

print("\nHere are the airports in the database:")
for icao_code, name in airports.items():
    print(f"{icao_code}: {name}")



"""
Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
 fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks 
 the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead,
  the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit,
   the program execution ends. The user can choose a new option as many times they want until they choose to quit. 
   (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. 
   You can easily find the ICAO codes of different airports online.)
"""

"""
2.An empty dictionary named airports is initialized to store ICAO codes and corresponding airport names.
11.If the user enters "1," they are prompted to enter the ICAO code and name of a new airport, and the information is added to the airports dictionary.
25.the program prints the ICAO codes and names of all airports stored in the airports dictionary.

"""