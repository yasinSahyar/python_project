##range   enumerate   zip

#range ---veri tipi

#range(10)
#range(0,10)
print(list(range(0,10)))  #range'i list'e cevirdik

print(list(range(12)))  #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print([*range(12)])     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print([*range(2,7)])    #[2, 3, 4, 5, 6]

for num in range(4):   #for oldugu icin list e cevrimeye gerek yok
    print(num)      #0,1,2,3

print("-----------------------------------------")

#enumerate

harfler = ['a','b','c','d','e']
for harf in enumerate(harfler):
    print(harf)     #(0, 'a') ,(1, 'b'),(2, 'c'),(3, 'd'),(4, 'e')

print("++++++++++++++++++++++++++++++++++++")

for index, harf in enumerate(harfler):
    print(index,harf)  #0 a ,1 b ,2 c, 3 d ,4 e

print("-------------zip----------------------------------")

ulkelr = ['TR','FR','DE','RUS','F','N','S','FIN']
siralamalar = range(1,9)

for ulke in zip(ulkelr,siralamalar):
    print(ulke)                       #('TR', 1),('FR', 2).....





