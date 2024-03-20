#map  filter ve lambda ifadeleri

print("-----------map , filter--------------")

def karesini_al(x):
    return x**2
print(karesini_al(5))       #25

sayilar = [*range(1,6)]
print(sayilar)              #[1, 2, 3, 4, 5]

print("++++++++++++++++")

sayilar = [*range(1,6)]
for index in range(len(sayilar)):
    sayilar[index] = karesini_al(sayilar[index])
    print(sayilar)

print("++++++map++++++++++")

sayilar = [*range(1,6)]
print([*map(karesini_al,sayilar)])         #[1, 4, 9, 16, 25]

def cifit_sayilari_filtrele(x):
    if x%2==0:
        return x
print(cifit_sayilari_filtrele(3))           # None


def cifit_sayilari_filtrele(x):
    return x if x%2==0 else None
print(cifit_sayilari_filtrele(10))          #10 , eger tak sayi versek None olyor

print("-------------lambda------------------")
sayilar = [*range(1,6)]
print(list(map(lambda x: x**2, sayilar)))     #[1, 4, 9, 16, 25]

print([*filter(lambda x: x if x%2==0 else None, sayilar)])  #[2, 4]



