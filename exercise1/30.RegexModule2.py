## https://www.youtube.com/watch?v=6yQQJBV1RpE&list=PLWctyKyPphPiul3WbHkniANLqSheBVP3O&index=32
#
import re

misal = "selam, benim telfon numaram +358-44985-7191"
patern = r"\+\d\d\d\-\d\d\d\d\d\-\d\d\d\d"                   #d -- rakam oldu icin kullanilir
print(re.search(patern,misal))

print("---------------------------")

cumle = "En sevdigim kanal base42."                          #w -- hem rakam hem karektir icin
patern = r"\s\w{5,}"            #\s\ onunde bosluk olan      #'w{5,}'---5 veya daha fazla arda arda gelen karektiri bul
                                                             # s --- space  yani bosluk
for eslesme in re.finditer(patern,cumle):
    print(eslesme.group(),eslesme.span())
    """
    sevdigim (2, 11)
    kanal (11, 17)
    base42 (17, 24)
    """

print("---------------? isareti ----------------------")

cumle1 = "En sevdigim kanal araba bwm 318,320,330,512,518,520,720 "
patern = r"\d?"                                             #\d? --  cumledeki sayi olanlari bul
for eslesme in re.finditer(patern,cumle1):
    print(eslesme.group(), eslesme.span())
    """
    ...
     (26, 26)
     (27, 27)
   3 (28, 29)
   1 (29, 30)
   8 (30, 31)
     (31, 31)
     ....
     parantez onunde sayi olan sayi oldugunu , parantez önu bos olan sayi olmadigini bildirir
    """