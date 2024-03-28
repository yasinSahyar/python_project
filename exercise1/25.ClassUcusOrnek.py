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
        return "{} sefer sayili {}-{} ucusmuz {} dakika surecektir".format(self.kod,self.kalkis,self.varis,self.sure)

ucus1 = Ucus('KLM245','LONDON','ANTALYA',253,300,150)
print(ucus1.anonus_yap())

ucus2 = Ucus('EP125','ISTANBUL','URUMQI',375,320,189)
print(ucus2.anonus_yap())