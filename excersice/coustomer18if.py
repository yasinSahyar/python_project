##

age = int(input("How old are you? "))

if age < 18:
    print("You will back home")
if 18 <= age  & age <= 20:
    ID= input("Do you have ID card? Yes/No")
    if ID == "Yes":
        print("ok, come in ")
    else:
        print("not ok, Go home and bring your ID")
else:
    print("Welcome to you!")