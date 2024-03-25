#soru cevaplar
print("------1--------")
def ustel_sayi1(a,b):
    return a**b
print(ustel_sayi1(3,2))

print("------2--------")

def ustel_sayi2(a,b):

    sonuc = 1
    if b < 1:
        return sonuc
    else:
        for kuvvet in range(1,b+1):
            sonuc = sonuc * a
        return sonuc
print(ustel_sayi2(5,3))


print("------3--------")

liste = [4,5,3,9,2,6,7,8,11]
liste.sort()              #otomatik siralama
def listedeki_enBuyuk_sayi(liste):
    liste.sort()
    return liste[-1],liste[-2]

print(listedeki_enBuyuk_sayi(liste))


print("------4--------")

def str_filtrele(list1):
    sonuc = []

    for x in list1:
        if type(x) == str:
            sonuc.append(x)
        else:
            pass
    return sonuc
print(str_filtrele([1,2,5,8,'abc','s',True]))