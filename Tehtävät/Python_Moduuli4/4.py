##
import random

def number_guessing_game():                                   ##The code defines a function isim
                                                     # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    while True:                                        ##无限循环make multiple guesses until they guess the correct number.
        user_guess = input("Guess the number (between 1 and 10): ")

        try:

            user_guess = int(user_guess)  ##user's input is converted to an integer using int(user_guess)

            # Check if the guess is correct
            if user_guess == secret_number:
                print("Correct! You guessed the right number.")
                break
            elif user_guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


number_guessing_game()




"""
Write a game where the computer draws a random integer between 1 and 10.
The user tries to guess the number until they guess the right number.
After each guess the program prints out a text: Too high, Too low or Correct.
 Notice that the computer must not change the number between guesses.

"""