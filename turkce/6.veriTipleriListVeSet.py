#list & set

list = ['a','b','c','d','e','f','h']
print(list) #['a', 'b', 'c', 'd', 'e', 'f', 'h']
print(list[3]) #d
print(list[-1]) #h
print(list[3]) #d

list = list + ['j','k']
print(list) # ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'j', 'k']
print(list[3:5]) #['d', 'e']

print("------------------------------------")

list.append('g')
print(list) #['a'......'j', 'k', 'g']

list.remove('g')
print(list)

list.pop() # listenin son elemanini siliyor
print(list) #['a', 'b', 'c', 'd', 'e', 'f', 'h', 'j']

list.pop(3)
print(list) #['a', 'b', 'c', 'e', 'f', 'h', 'j']

print("--------------------------------")

sayilar = [123,154,1658,254,654,327,575]
sayilar.sort() #siralama
print(sayilar) #[123, 154, 254, 327, 575, 654, 1658]

sayilar.reverse() #teris siralama
print(sayilar) #[1658, 654, 575, 327, 254, 154, 123]

print("----------------------------------------")

#set


