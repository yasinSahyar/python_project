##
import mysql.connector

# Establish a connection to the database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Dimayman1',
    autocommit=True
)

def fetch_airport_info(icao_code):
    try:
        cursor = connection.cursor()
        query = f"SELECT name, municipality FROM airport WHERE ident = '{icao_code}'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            airport_name, location = result
            print(f"Airport Name: {airport_name}")
            print(f"Location (Town): {location}")
        else:
            print(f"No airport found with ICAO code '{icao_code}'.")

    except Exception as e:
        print(f"Error fetching data: {e}")

    finally:
        cursor.close()


user_icao_code = input("Enter the ICAO code of an airport: ").strip().upper()
fetch_airport_info(user_icao_code)





"""
Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out
the corresponding airport name and location (town) from the airport database used on this course.
The ICAO codes are stored in the ident column of the airport table.
"""

"""
14.This function takes an ICAO code as input and fetches the corresponding airport name and location (town) from the database.
17.Executing a query to fetch airport information
35..strip()--bosluklari kaldirmak ,   .upper() ---girdigi harifi buyuk yapma


"""

