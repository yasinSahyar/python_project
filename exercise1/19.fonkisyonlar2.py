##

def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b

print(buyuk_sayi_dondur(5,10))        #10
def metin_yazdir(a,b):
    buyuk_sayi =buyuk_sayi_dondur(a,b)
    sablon_metin = "{} daha buyuk sayidir".format(buyuk_sayi)
    print(sablon_metin)

metin_yazdir(5,10)

print("---------fonkisyon birden fazla sonucu dondurebilir--------")

print("yasin sahyar".split())   #['yasin', 'sahyar']      1.usul

def isim_soyisim_ayirma(isim_soyisim):                    #2.usul
    isim=isim_soyisim.split()[0]
    soyisim=isim_soyisim.split()[1]
    return isim,soyisim
print(isim_soyisim_ayirma("isa memet"))  #('isa', 'memet')


a,b = isim_soyisim_ayirma("kamal bilal")
print(a)   #kamal
print(b)   #bilal

print("+++++++++args arguman ++++birlestirme ++++++++")

print("_".join(["isa","bilal"]))     #isa_bilal      1.usul

def isim_soyisim_birlestir(isim,soyisim):             #2.usul
    return "_".join([soyisim,isim])
print(isim_soyisim_birlestir("kurban","rishit"))    #rishit_kurban






