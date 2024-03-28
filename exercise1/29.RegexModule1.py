#REgular Expressions(REGEX) --re
#yazinin icersinde belirli kosulari saglayan kelimeleri filtirlemek icin (kac defa kulanildi gibi)

import re

cumle = "Mustafa Kemal Ataturk, Turk asker,devlet adami ve Turkiye Cumhuryetinin kurucusudur."
patern = "Turk"   #yukardaki cumlede "Turk" kelimesi kac tane var oni bulmak icin

print(re.search(patern,cumle))          #<re.Match object; span=(23, 27), match='Turk'>

durum = re.search(patern,cumle)
print(durum.span())                       #(23, 27)

print(durum.start())                    #23

print(durum.end())                      #27
print(durum.group())                   #Turk

print("--------coklu eslesmelerde(match)-----------")

for eslesme in re.findall(patern,cumle):
    print(eslesme)                    #Turk  ,Turk

for eslesme in re.finditer(patern,cumle):
    print(eslesme.span(),eslesme.group())
    #(23, 27) Turk
    #(50, 54) Turk


print("--------ornek--------------")

#ornek = "base42"
#patern = "base\d\d"
misal = "selam, benim telfon numaram +358-44985-7191"
patern = r"\+\d\d\d\-\d\d\d\d\d\-\d\d\d\d"
print(re.search(patern,misal))                   #<re.Match object; span=(28, 42), match='+358-44985-7191'>




# https://www.youtube.com/watch?v=bKWzIvYZmfA&list=PLWctyKyPphPiul3WbHkniANLqSheBVP3O&index=31