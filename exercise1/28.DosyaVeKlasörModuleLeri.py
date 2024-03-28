#https://www.youtube.com/watch?v=5aaPdOIZKIA&list=PLWctyKyPphPiul3WbHkniANLqSheBVP3O&index=30
#OS - modulu
# %ls -- listele
#%pwd  -- dosyanin adresini gozlemlemek icin
import os
print(os.getcwd())                 # suanki dosyariminin adresi

print(os.listdir())                 #ayni pakege icindeki tum deger dosyalr

print(os.listdir('C:\\Users'))      #C:\\Users--icindeki tum dosyalar ['All Users', 'Default', 'Default User', 'desktop.ini', 'hallo', 'hello', 'Public', 'yasin']

dosyalar = os.listdir()
for elaman in dosyalar:
    print(elaman + 'yasin')   #pakegediki tum dosyalarin ismini arkasina 'yasin' eklicek

print("---------yeni kilasor olusturmak------------")

#print(os.mkdir())     #yeni dosya olusturmak icin

#print(os.rmdir())     #dosya silmek

print("---------yeni dosya olusturmak------------")

yeni_dosya = os.open('yeni_dosya.txt',os.O_RDWR|os.O_CREAT)
print(os.write(yeni_dosya, 'Hello World!'.encode()))
print(os.close(yeni_dosya))

#dosya nin icindeki yaziyi okutma

yeni_dosya = os.open('yeni_dosya.txt',os.O_RDONLY)
uzunluk = os.stat(yeni_dosya).st_size
icerik = os.read(yeni_dosya,uzunluk)
print(icerik.decode())                           #Hello World!
print(os.close(yeni_dosya))



