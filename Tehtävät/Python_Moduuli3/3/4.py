def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # Check if the year is divisible by 100 and not divisible by 400
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def main():
    # Ask the user to enter a year
    year = int(input("Enter a year: "))

    # Check if the entered year is a leap year
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()
