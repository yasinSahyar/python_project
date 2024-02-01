##

kulanici1 = {
    'ad' : 'Yasin',
    'soyad' : 'Sahyar'
}
print(kulanici1)
print(kulanici1.values()) ##dict_values(['Yasin', 'Sahyar'])

print("-------------------------")

for k, v in kulanici1.items():
    print("key =", k, "value =", v)
