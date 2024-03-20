"""
Kirjoita alla olevaan ohjelmaan puuttuvat kaksi funktiota siten, että ohjelma toimil esimerkin mukaisesti.
Funktioiden on toimittava semanttisesti oikein myös, jos ohjelmakoodissa esiintyvät lukuarvot vaihtuisivat.
"""
# Ohjelma:
def suorakulmion_piiri(sivu1, sivu2):
    return 2 * (sivu1 + sivu2)
def parittomat(lista):
    return [luku for luku in lista if luku % 2 != 0]
#Koodaa tähän:
sivu1 = 7
sivu2 = 3

print (f"Suorakulmion sivut ovat {sivu1} ja {sivu2}")
print (f"Suorakulmion piiri on {suorakulmion_piiri(sivu1, sivu2)}")

luvut = [12, 5, 21, 4, 8, 0, 11]

parittomat = parittomat (luvut)

print ("Alkuperäiset luvut: " + str(luvut))
print ("Parittomat luvut: " + str(parittomat))

"""
Tuloste:

Suorakulmion sivut ovat 7 ja 3 
Suorakulmion piiri on 20
Alkuperäiset luvut: [12, 5, 21, 4, 8, 0, 11]
Parittomat luvut:[5,21,11]
"""