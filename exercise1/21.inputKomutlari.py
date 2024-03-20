##
"""
girdi = input("bir sayi giriniz:")
print(girdi)
"""


def uygulama():
    girdi = input("bir sayi giriniz:")
    islem = input("verilerin tek mi cifit mi oldugunu sorgula:")

    if islem=='cifit':
        if int(girdi)%2==0:
            return 'evet {} bir cifit sayidir'.format(girdi)
        else:
            return 'hayir {} bir cifit sayi degildir'.format(girdi)
    elif islem=='tek':
        if int(girdi)%2==1:
            return 'evet {} bir tek sayidir'.format(girdi)
        else:
            return 'hayir {} bir tek sayi degildir'.format(girdi)
print(uygulama())