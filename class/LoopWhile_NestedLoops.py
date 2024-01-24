##

first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first*second:d}")
        second = second + 1
    first = first + 1

    """
    1 times 1 is 1
    1 times 2 is 2
    1 times 3 is 3
    1 times 4 is 4
    1 times 5 is 5
    ......
    5 times 3 is 15
    5 times 4 is 20
    5 times 5 is 25
    """

    print("---------------------------------------")

