##
names = set()
while True:                           ##无限循环infnt--executing until explicitly terminated.
    name = input("Enter a name: ")
    if not name:
        break
    if name in names:                           #Checking for Existing Names
        print(f"{name} is an existing name.")
    else:
        print(f"{name} is a new name.")
        names.add(name)

print("\nHere are the names you entered:")
for name in names:                                                       ##iterates through the set names
    print(name)




"""
Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the program 
either prints out New name or Existing name depending on whether the name was entered for the first time. Finally,
 the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names.
"""

"""
2.An empty set named names is initialized. This set will be used to store unique names entered by the user.
14.iterates through the set names and prints each unique name.

"""