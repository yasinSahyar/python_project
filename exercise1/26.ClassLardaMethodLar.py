class Ucus():
    hayayolu = "FINAIR"
    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod = kod
        self.kalkis= kalkis
        self.varis= varis
        self.sure= sure
        self.kapasite= kapasite
        self.yolcu= yolcu
    def anonus_yap(self):
        return "{} sefer sayili {}-{} ucusmuz {} dakika surecektir".format(
            self.kod,
            self.kalkis,
            self.varis,
            self.sure)

    def koltuk_sayisi_guncelleme(self):
        return self.kapasite - self.yolcu

    def bilet_satis(self,bilet_adedi = 1):
        #self.yolcu = self.yolcu + bilet_adedi
        if self.yolcu + bilet_adedi <= self.kapasite:
         self.yolcu += bilet_adedi
         self.koltuk_sayisi_guncelleme()
         print('{} adet bilet satilmistir,kalan koltuk sayisi {}'.format(
             bilet_adedi,
             self.koltuk_sayisi_guncelleme()))
        else:
            print('Islem gerceklestirilemedi,yetersiz koltuk sayisi....')

    def bilet_iptal(self,bilet_adedi = 1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            print('{} adet bilet iptal edilmistir,guncel koltuk sayisi {}'.format(
                bilet_adedi,
                self.koltuk_sayisi_guncelleme()))
        else:
            print('Iptal gerceklestirilemedi,iptal edilecek kadar yolcu yok')



ucus1 = Ucus('EP125','ISTANBUL','URUMQI',375,320,189)
print(ucus1.anonus_yap())

ucus2 = Ucus('EP225','ISTANBUL','KASHGAR',325,320,199)
print(ucus2.koltuk_sayisi_guncelleme())

ucus3 = Ucus('EP225','ISTANBUL','KASHGAR',325,320,199)
print(ucus3.koltuk_sayisi_guncelleme())

print(ucus3.bilet_satis(15))            #15 adet bilet satilmistir,kalan koltuk sayisi 106

print(ucus3.bilet_satis(46))            #46 adet bilet satilmistir,kalan koltuk sayisi 60

print(ucus3.bilet_iptal(2))           #2 adet bilet iptal edilmistir,guncel koltuk sayisi 62

print(ucus3.bilet_satis(7))            #7 adet bilet satilmistir,kalan koltuk sayisi 55

print(ucus3.bilet_iptal(8))            #8 adet bilet iptal edilmistir,guncel koltuk sayisi 63

