import mysql.connector
from geopy.distance import geodesic
import random

# Establish a connection to the database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Dimayman1',
    autocommit=True
)

def fetch_airport_coordinates(icao_code):
    try:
        cursor = connection.cursor()
        query = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident = '{icao_code}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            latitude, longitude = result
            return latitude, longitude
        else:
            print(f"No airport found with ICAO code '{icao_code}'.")
            return None, None

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None

    finally:
        cursor.close()

def calculate_distance(coord1, coord2):
    if coord1 and coord2:
        return geodesic(coord1, coord2).kilometers
    else:
        return None

def select_random_target():
    cursor = connection.cursor()
    cursor.execute("SELECT ident FROM airport ORDER BY RAND() LIMIT 1")
    target_icao = cursor.fetchone()[0]
    cursor.close()
    return target_icao

def flight_game():
    print("Welcome to the Flight Game!")
    print("You need to find a hidden target city with an airport within 5 flight rights.")
    print("Each flight will reveal how far you are from the target.")

    target_icao = select_random_target()
    target_coords = fetch_airport_coordinates(target_icao)
    flight_count = 0

    while flight_count < 5:
        print("\nFlight number:", flight_count + 1)
        if target_coords:
            distance_to_target = calculate_distance(target_coords, fetch_airport_coordinates(target_icao))
            print("Distance to target:", distance_to_target, "kilometers")
        else:
            print("Unable to calculate distance to target.")

        # Ask user for input
        user_input = input("Enter the name of a city closest to the target: ").strip().title()

        # Check if user has reached the target
        if user_input.upper() == target_icao:
            print("\nCongratulations! You have reached the target!")
            return

        flight_count += 1

    print("\nYou lost in this game. Try again.")

if __name__ == "__main__":
    flight_game()
