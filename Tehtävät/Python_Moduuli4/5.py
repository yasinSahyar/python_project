##
def check_password_strength(password): #密码格式
    # Password rules: At least 8 characters, containing at least one uppercase letter and one digit
    return len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password)

def login_program():
    max_attempts = 5                               ##stores the maximum number of login attempts allowed
    current_attempt = 0                            ##how many input calculate

    correct_username = "yasin"
    correct_password = "pas123"

    while current_attempt < max_attempts:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == correct_username and password == correct_password:
            print("Welcome!")
            break
        else:
            print("Incorrect username or password. Please try again.")
            current_attempt += 1

    if current_attempt == max_attempts:
        print("Access denied. Maximum attempts reached.")


login_program()



"""
Write a program that asks the user for a username and password. If either or both are incorrect,
 the program ask the user to enter the username and password again. This continues until the login information is correct
 or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome.
 After five failed attempts the program prints out Access denied. The correct username is python and password rules.
"""

"""
4.This function checks the strength of a password based on certain rules:
The password must be at least 8 characters long.
It must contain at least one uppercase letter.
It must contain at least one digit.
The function returns True if the password meets these criteria and False otherwise.


"""