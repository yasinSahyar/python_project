##

def laskeAla(kanta, korkesu):
    ala = kanta * korkesu
    return ala

suorakaiteen_kanta = float(input("anna kanta"))
suorakaiteen_korkesu =float(input("anna korkesu"))

vastus = laskeAla(suorakaiteen_kanta, suorakaiteen_korkesu)
print(f"vastus = {vastus}")