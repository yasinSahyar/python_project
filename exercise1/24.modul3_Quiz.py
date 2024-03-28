#soru cevaplar
print("------1--------")
def ustel_sayi1(a,b):
    return a**b
print(ustel_sayi1(3,2))                      #9

print("------2--------")

def ustel_sayi2(a,b):

    sonuc = 1
    if b < 1:
        return sonuc
    else:
        for kuvvet in range(1,b+1):
            sonuc = sonuc * a
        return sonuc
print(ustel_sayi2(5,3))                            #125


print("------3--------")

liste = [4,5,3,9,2,6,7,8,11]
liste.sort()              #otomatik siralama
def listedeki_enBuyuk_sayi(liste):
    liste.sort()
    return liste[-1],liste[-2]

print(listedeki_enBuyuk_sayi(liste))                           #(11, 9)


print("------4--------")

def str_filtrele(list1):
    sonuc = []

    for x in list1:
        if type(x) == str:
            sonuc.append(x)
        else:
            pass
    return sonuc
print(str_filtrele([1,2,5,8,'abc','s',True]))                    #['abc', 's']


print("------5--------")


def paradan_alti_sifiri_at(list2):
    sonuc2 = []
    for x in list2:
        sonuc2.append(x/1000000)
    return sonuc2
print(paradan_alti_sifiri_at([1000000,9500000,15000000]))         #[1.0, 9.5, 15.0]


print("------6--------")

def zaman_verisi_al():
    saat = input("saat giriniz:")
    if saat.isdigit():
        saat = int(saat)
        if((saat >= 0) and (saat < 24)):
            dakika = input('dakika giriniz:')
            if dakika.isdigit():
                dakika = int(dakika)
                if ((dakika >= 0) and (dakika < 60)):
                    return 'Giris yapilan zaman {}:{}'.format(saat,dakika)
                else:
                    return 'Girilen dakika araligi yanlis'
            else:
                return 'Girilen dakika  yanlis veri tipinde'
        else:
            return 'Girilen saat araligi yanlis'
    else:
        return 'Girilen saat  yanlis veri tipinde'

print(zaman_verisi_al())