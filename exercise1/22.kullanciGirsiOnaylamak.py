#

def sayi_girdisi_kontrol():
    girdi = input("bir sayi giriniz:")

    if girdi.isdigit():                 # 'isdigit'---vaiable is intger or string sorgusunu yapar
        print("tebrikler! sayi tipi deger girdiniz...")
    else:
        print("uzgunum! bu bir sayi tipi degisken degildir...")

def sayi_girdisi_kontrol_dongusu():
    girdi = input("sayi giriniz:")
    while not girdi.isdigit():
        print("uzgunum! bu bir sayi tipi degisken degildir...")
        girdi = input("sayi giriniz:")
    else:
        print("tebrikler! sayi tipi deger girdiniz...")


# sayi_girdisi_kontrol()
sayi_girdisi_kontrol_dongusu()

print("-----------------------------")
def eposta_kontrol():
    giris = input("gecerli bir email adresi giniz:")
    # yasin@gmail.com -- '@' '.' olmasi gerekir
    while not (('@' in giris) and ('.' in giris)):
        print("uzgunum! gecerli email adresi degildir...")
        giris = input("gecerli bir email adresi giniz:")

    else:
        print("tebrikler! gecerli eposta adresi girdiniz...")

eposta_kontrol()