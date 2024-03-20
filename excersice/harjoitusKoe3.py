"""
Haluat Python-ohjelman tulostavan relaatiotietokannassa olevan taulukon sisällön. Esitä neljä keskeist
vaihetta tai toimenpidettä, jotka Python-ohjelmoijan on tätä varten toteutettava ohjelmakoodissa
"""
"""
You want a Python program to print the contents of a table in a relational database. List the four main ones
step or action that the Python programmer must implement in the program code for this
"""

"""
1.Establishing a Database Connection:  Tietokantayhteyden muodostaminen
2.Retrieving Table Data:               Taulukon tiedon hakeminen:
3.Processing the Results:              Tulosten käsittely:
4.Printing:                            Tulostaminen:
 
"""
import sqlite3

# Establish a connection to an SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Retrieve table data
cursor.execute('SELECT * FROM table_name')
rows = cursor.fetchall()

# Print the table content
for row in rows:
    print(row)

# Close the connection
conn.close()
