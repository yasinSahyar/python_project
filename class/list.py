##
names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
print(names)
print(len(names)) ##5
print(names[2])

print(names[-4]) ##Ahmed

print(names[1:3]) ##['Ahmed', 'Pekka']

print(names[2:]) ##['Pekka', 'Olga', 'Mary']

print("---------------------------------------------------")

names = []

name = input("Enter the first name or quit by pressing Enter: ")
while name!="":
    names.append(name) ##listige kushush
    name = input("Enter the next name or quit by pressing Enter: ")

print(names) ##['isa', 'kemal', 'yasin']

