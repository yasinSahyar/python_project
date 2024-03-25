

print(round(1.6))    #2 ye yakin oldugu icin 2 olucak
print(round(3.4))     # 3 e yakin oldugu icin 3 olucak

def tam_sayiya_cevir():
    girdi = input("bir onadalik sayi girniz:")

    print("yuvarlama isleminin sonucu:{}".format(round(float(girdi))))
    #harif girersek hata aliriz

tam_sayiya_cevir()

print("---------try -- hatayi atlamak icin-----------------")

def tam_sayiya_cevir2():
    giris = input("bir onadalik sayi girniz:")

    try:
        giris = float(giris)
        print("yuvarlama isleminin sonucu:{}".format(round(float(giris))))
    except:        #haricinde
        print("{} girdiniz veri tipini ondalik sayiya cevrilemyor".format(giris))
     #burda harif girersek hata almadan sadece uyari alyoruz

tam_sayiya_cevir2()


print("---------finally -- ")

def tam_sayiya_cevir3():
    giris3 = input("bir onadalik sayi girniz:")
    status = ''
    try:
        giris3 = float(giris3)
        print("yuvarlama isleminin sonucu:{}".format(round(float(giris3))))
        status = 'basarli'
    except:        #haricinde
        print("{} girdiniz veri tipini ondalik sayiya cevrilemyor".format(giris3))
        status = 'basarsiz'
    finally:
        print('tam sayiya cevirme islemi {} olarak tamamlandi!'.format(status))

tam_sayiya_cevir3()



print("---------dongu -- ")


def tam_sayiya_cevir_dongu():

    while True:                   #bir sayi girene kadar devam edecek
         giris1 = input("bir onadalik sayi girniz:")

         try:
            giris1 = float(giris1)
            print("yuvarlama isleminin sonucu:{}".format(round(float(giris1))))
            break
         except:        #haricinde
            print("{} girdiniz veri tipini ondalik sayiya cevrilemyor".format(giris1))
            pass

tam_sayiya_cevir_dongu()