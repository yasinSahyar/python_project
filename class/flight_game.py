import mysql.connector

def haeKentta(nimi):
    sql = "select name,ident from airport where name like '%" + nimi +"%'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Hakemasi lentokentän koko nimi on {rivi[0]} ja sen ICAO koodi on{rivi[1]}.")
    return

def hae(sql):
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Dimayman1',
         autocommit=True
         )
while True:
    print("1: kentän suppeat tiedot nimellä")
    print("2: kentän laajat tiedot nimellä")
    print("3: poistu")

    kentanNimi = input("Annan kentän nimellä")
    valinta = input("Valitse 1 tai 2")
    if valinta == "1":
        haeKentta(kentanNimi)
    elif valinta == "2":
        sql = "select ident, airport.name, country.name from airport, country where airport.iso_country = country.iso_country and airport.name like '%" + kentanNimi +"%'"
        print(sql)
        tulos = hae(sql)
        for rivi in tulos:
            print(rivi[0], rivi[1], rivi[2])


    elif valinta == "3":
        break

    else:
        print("Annoit virheellisen syötten")










kentanNimi = input("Anna kentan nimi")
haeKentta(kentanNimi)