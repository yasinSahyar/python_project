##
import mysql.connector
from geopy.distance import geodesic                        #calculating the distance between two geographic coordinates.


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

if __name__ == "__main__":
    icao_code1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    icao_code2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    coord1 = fetch_airport_coordinates(icao_code1)
    coord2 = fetch_airport_coordinates(icao_code2)

    distance_km = calculate_distance(coord1, coord2)

    if distance_km is not None:
        print(f"Distance between {icao_code1} and {icao_code2}: {distance_km:.2f} kilometers")
    else:
        print("Unable to calculate distance due to missing coordinates.")




"""
Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between
the two airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate
the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the library by selecting
View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.
"""

"""
16.This function takes an ICAO code as input, fetches the latitude and longitude coordinates of the corresponding airport from the database, and returns them

37.This function takes two sets of coordinates as input and calculates the distance between them using the geodesic function from geopy.distance.
"""