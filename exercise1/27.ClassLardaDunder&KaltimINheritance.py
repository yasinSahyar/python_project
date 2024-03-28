#dunder method "__" --
#https://www.youtube.com/watch?v=OAxdvmQaYO0&list=PLWctyKyPphPiul3WbHkniANLqSheBVP3O&index=29
class Ucus():
    hayayolu = "FINAIR"
    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod = kod
        self.kalkis= kalkis
        self.varis= varis
        self.sure= sure
        self.kapasite= kapasite
        self.yolcu= yolcu

    def __repr__(self):
        return "{} sefer sayili ucus sistemde olusturulmustur..".format(self.kod)

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
print(ucus1.anonus_yap())            #EP125 sefer sayili ISTANBUL-URUMQI ucusmuz 375 dakika surecektir

ucus2 = Ucus('TK125','ISTANBUL','HELSINKI',375,320,189)
print(ucus2)         #13.14 teki fonkisyon sayesinde---    #TK125 sefer sayili ucus sistemde olusturulmustur..

print("-------------Inheritence-------------------------")
# Inheritance(kalitim)
class Seyahat():
    def __init__(self,kalkis,varis):
        self.kalkis= kalkis
        self.varis= varis
    def anonus(self):
        return "{}--{} seyahetine hosgeldiniz!".format(self.kalkis,self.varis,)
class Otobus(Seyahat):
    def __init__(self,mola_duraklari,kalkis,varis):
        Seyahat.__init__(self,kalkis,varis)         #Seyahat in yeni ornegini olusturyoruz
        self.mola_duraklari = mola_duraklari
        self.kalkis = kalkis
        self.varis = varis

seyahat1 = Seyahat('ANTALYA','BODRUM')
print(seyahat1.anonus())                          #ANTALYA--BODRUM seyahetine hosgeldiniz

otobus1 = Otobus(['MARMARIS','FETHIHYE','CESME'],'ANTALYA','BODRUM')
print(otobus1.mola_duraklari)

