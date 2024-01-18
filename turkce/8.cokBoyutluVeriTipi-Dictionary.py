#cok boyutlu veri tipi ---Dictionary

dict1 = {
         'isim' : 'kemal',
         'yas' : 35,
         'lokasyon' : 'Helsinki'
}
print(dict1['isim']) #kemal


print("--------------------------------------------")


dict2 = {
         'isim' : 'yasin',
         'yas' : 35,
         'dogum yeri' : 'xinjiang',
         'yasadigi yer' : 'Helsinki'
}
print(dict2)

print("--------------------------------------------")


dict3 = {
         'isim' : 'yasin',
         'yas' : 35,
         'lokasyon' : {
                  'dogum yeri' : 'xinjiang',
                'yasadigi yer' : 'Helsinki'
         }
}
print(dict3) #{'isim': 'yasin', 'yas': 35, 'lokasyon': {'dogum yeri': 'xinjiang', 'yasadigi yer': 'Helsinki'}}


print(dict2['yas']) #35
print(dict3['lokasyon']) #{'dogum yeri': 'xinjiang', 'yasadigi yer': 'Helsinki'}
print(dict3['lokasyon']['dogum yeri']) #xinjiang
print(dict1['isim']) #kemal

print(dict3.get('lokasyon').get('dogum yeri')) #xinjiang


print(dict2.keys()) #dict_keys(['isim', 'yas', 'dogum yeri', 'yasadigi yer'])
print(dict2.values()) #dict_values(['yasin', 35, 'xinjiang', 'Helsinki'])

print(dict2.items()) #dict_items([('isim', 'yasin'), ('yas', 35), ('dogum yeri', 'xinjiang'), ('yasadigi yer', 'Helsinki')])


