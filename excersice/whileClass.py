import random
dice1 = dice2 = rolls = 0
while (dice1!=6 or dice2!=6):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    rolls = rolls + 1
print(f"Rolled {rolls:d} times.")


print("-----------------------------------")


first = 1
while first <= 3:
    second = 1
    while second <= 3:
        print(f"{first} times {second} is {first*second:d}")
        second = second + 1
    first = first + 1

print("------------------------------------------")



