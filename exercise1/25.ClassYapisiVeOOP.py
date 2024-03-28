# class

class Ucus():
    hayayolu = "THY"
    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod = kod
        self.kalkis= kalkis
        self.varis= varis
        self.sure= sure
        self.kapasite= kapasite
        self.yolcu= yolcu

ucus1=Ucus('TK123','ISTANBUL','ANKARA',60,320,152)
print(ucus1.hayayolu)
print(ucus1.sure)
print(ucus1.kalkis)
print(ucus1.varis)
print(ucus1.kapasite)
print(ucus1.yolcu)

ucus2=Ucus('EL123','HELSINKI','PARIS',55,250,180)
print(ucus2.hayayolu)
print(ucus2.sure)
print(ucus2.kalkis)
print(ucus2.varis)
print(ucus2.kapasite)
print(ucus2.yolcu)



