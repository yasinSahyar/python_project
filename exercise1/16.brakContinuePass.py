## break
harifler = ['a','b','c','d','e'] * 30
for index,harf in enumerate(harifler):
    if harf == 'c':
        print('{} harf {}. indexte'.format(harf,index))     ##c harf 2. indexte
        break


##continue

for sayi in range(1,6):
    if sayi%2==0:           #cifit sayi sorgulama
        continue
    print(sayi)             #1,3,5


##pass


for sayi2 in range(7,15):
    if sayi2%2==0:           #cifit sayi sorgulama
        pass
    else:
        print(sayi2)           # 7,9,11,13

