## loop -- dongu

yourum_brakanlar = ["yasin esmet","emer yasin","kemal bilal","isa memet","tunyaz lohman","ayjamal ehmet","bilikiz kasim"]

for kullanci in yourum_brakanlar:
    print(kullanci)

kullanci_sayisi = 0
for kullanci in yourum_brakanlar:
    kullanci_sayisi = kullanci_sayisi + 1
    print(kullanci_sayisi,kullanci)
    """
    1 yasin
    2 emer
    3 kemal
    4 isa
    5 tunyaz
    6 ayjamal
    7 bilikiz

    """
    print("-------------------------------")

    print(yourum_brakanlar[0].split()) ##['yasin', 'esmet']


    kullanci_sayisi = 0
    for kullanci in yourum_brakanlar:
        kullanci_sayisi = kullanci_sayisi + 1
        ad, soyad = kullanci.split()[0], kullanci.split()[1]
        print('{0}, kullanicinin adi {1} ve soyadi {2}'.format(kullanci_sayisi,ad, soyad))


    print("-------------------------------------")

    moderator = "yasin esmet"
    kullanci_sayisi = 0
    moderator_sayisi = 0

    for kullanci in yourum_brakanlar:

        ad, soyad = kullanci.split()[0], kullanci.split()[1]

        if(kullanci == moderator):
            moderator_sayisi += 1 ##moderator_sayisi = moderator_sayisi + 1

            print('{0}, moderator adi {1} ve soyadi {2}'.format(moderator_sayisi,ad, soyad))

        else:
            kullanci_sayisi += 1
            print('{0}, kullanici adi {1} ve soyadi {2}'.format(kullanci_sayisi, ad, soyad))









