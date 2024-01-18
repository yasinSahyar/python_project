##Tehtävä5

## Ask the user for mass in medieval units
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# Conversion factors
pounds_per_talent = 20
lots_per_pound = 32
grams_per_lot = 13.3

# Calculate the total mass in grams
total_grams = (talents * pounds_per_talent + pounds) * lots_per_pound * grams_per_lot + lots * grams_per_lot

## Convert grams to kilograms and remaining grams
total_kilograms = total_grams // 1000
remaining_grams = total_grams % 1000

## result
print(f"The weight in modern units:")
print(f"{int(total_kilograms)} kilograms and {remaining_grams:.2f} grams.")
