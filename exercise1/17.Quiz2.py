##
kullanici1 = {
    'ad': 'isa',
    'soyad':'memet',
    'uzmanlik':['Front-end']
}
kullanici2 = {
    'ad': 'kemal',
    'soyad':'bilal',
    'uzmanlik':['Tasarim']
}
kullanici3 = {
    'ad': 'emer',
    'soyad':'yasin',
    'uzmanlik':['Front-end']
}
kullanici4 = {
    'ad': 'yasin',
    'soyad':'exmet',
    'uzmanlik':['Back-end']
}
print("-------------- kullanici1 in uzmanlik  ve ad ni yazdir --------------------------")

print(kullanici1.get('uzmanlik'))                              #['Front-end']
print(kullanici1.get('ad'))                                    #isa

print("++++++++++++++++ 'Front-end' olanlarin adi +++++++++++++++++")

kullanici_listesi = [kullanici1,kullanici2,kullanici3,kullanici4]
for kullanici in kullanici_listesi:
    if kullanici.get('uzmanlik') == ['Front-end']:
        print(kullanici.get('ad'))                             # isa , emer


print("++++++++++++++++ 'Back-end' olanlarin adi +++++++++++++++++")

kullanici_listesi = [kullanici1,kullanici2,kullanici3,kullanici4]
for kullanici in kullanici_listesi:
    if kullanici.get('uzmanlik') == ['Back-end']:
        print(kullanici.get('ad'))                             # yasin


print("++++++++++++++++ yas eklemek +++++++++++++++++")

kullanici_yaslari_listesi = [22,34,30,28]

for kullanici ,yas in zip(kullanici_listesi,kullanici_yaslari_listesi):
    if yas < 25:
        print(kullanici)
        #{'ad': 'isa', 'soyad': 'memet', 'uzmanlik': ['Front-end']}


print("++++++++++++++++ asal sayi +++++++++++++++++")

deger = 5
x =deger -1
while x > 1:
    if deger %x == 0:
        print('{} sayi asal dagil!'.format(deger))
        break
    else:
        x -= 1

else:
        print('{} sayi asaldir!'.format(deger))