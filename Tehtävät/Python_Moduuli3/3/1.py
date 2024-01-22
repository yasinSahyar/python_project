##

def main():
    # Ask the fisher for the length of the zander in centimeters
    zander_length = float(input("Enter the length of the zander in centimeters: "))

    # Check if the zander meets the size limit
    if zander_length >= 42:
        print("Congratulations! The zander is of legal size.")
    else:
        # Calculate how many centimeters below the size limit the zander is
        below_limit = 42 - zander_length

        # Instruct to release the fish back into the lake
        print("Please release the zander back into the lake.")

        # Notify the user of how many centimeters below the size limit the zander is
        print(f"The zander is {below_limit:.2f} centimeters below the size limit.")


if __name__ == "__main__":
    main()
