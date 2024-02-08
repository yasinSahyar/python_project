## fonkisyon--cagirp kullanabilmemiz icin

# def (define)--fonkisyonu --yani tanitmak
def bes_bastir():
    print(5)
bes_bastir()   #5

print("----------return ile print farki----------")

def bes_dondur():
    return 5
bes_dondur()     #

a = bes_dondur()
print(a)                 #5

print("++++++++++++fonkisyon argumanlari+++++++++++++")

def sayi_dondur(sayi):
    return sayi
print(sayi_dondur(10))    #10

def sayi_dondur(sayi=250):
    return sayi
print(sayi_dondur(89))       #89  - eger sayi vermeseyidik 250 yazardi

print("--------------------")

def buyuk_sayi_dondur(a,b):
    if a>b:
        return a
    elif b>a:
        return b

print(buyuk_sayi_dondur(5,10))        #10