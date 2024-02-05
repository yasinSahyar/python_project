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





