def main():
    # Ask the user for biological gender and hemoglobin value
    gender = input("Enter biological gender (M/F): ").upper()
    hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))

    # Define normal hemoglobin ranges for males and females
    normal_range_male = (134, 167)
    normal_range_female = (117, 155)

    # Check gender and hemoglobin value
    if gender == "M":
        if normal_range_male[0] <= hemoglobin_value <= normal_range_male[1]:
            print("Hemoglobin level is normal for adult males.")
        elif hemoglobin_value < normal_range_male[0]:
            print("Hemoglobin level is low for adult males.")
        else:
            print("Hemoglobin level is high for adult males.")
    elif gender == "F":
        if normal_range_female[0] <= hemoglobin_value <= normal_range_female[1]:
            print("Hemoglobin level is normal for adult females.")
        elif hemoglobin_value < normal_range_female[0]:
            print("Hemoglobin level is low for adult females.")
        else:
            print("Hemoglobin level is high for adult females.")
    else:
        # Handle invalid gender input
        print("Error: Invalid gender input.")

if __name__ == "__main__":
    main()
