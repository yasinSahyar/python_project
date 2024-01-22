def main():
    # Ask the user to enter the cabin class
    cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")

    # Check the cabin class and print the corresponding description
    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
    else:
        # Handle invalid cabin class
        print("Error: Invalid cabin class.")

if __name__ == "__main__":
    main()
