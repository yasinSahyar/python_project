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

def fetch_airports_by_country(area_code):
    try:
        cursor = connection.cursor()
        query = f"""SELECT type, COUNT(*) AS num_airports FROM airport WHERE iso_country = '{area_code}' GROUP BY type ORDER BY num_airports DESC """
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            print(f"Airports in {area_code} ordered by type:")
            for row in results:
                airport_type, num_airports = row
                print(f"{airport_type.capitalize()}: {num_airports} airports")
        else:
            print(f"No airports found for area code '{area_code}'.")

    except Exception as e:
        print(f"Error fetching data: {e}")

    finally:
        cursor.close()


user_area_code = input("Enter the area code (e.g., FI,TR,CN): ").strip().upper()
fetch_airports_by_country(user_area_code)

"""
Write a program that asks the user to enter the area code (for example FI) and prints out the airports located
in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.
"""

"""
17.The SQL query string is constructed to select the type of airport and count the number of airports of each type in the specified country (identified by the area code).
21.If airports are found for the specified area code , the function prints the airport type along with the number of airports of that type. 
29.Any exceptions that occur during the execution of the database operations are caught and handled, printing an error message. 

"""