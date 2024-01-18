#sabit koleksiyon veri tipleri --Tuple

list = ['a','b','c','d','e','a']
print(list)

tup = ('a','b','c','d','e','a')
print(tup)

list[0] = 125
print(list) #[125, 'b', 'c', 'd', 'e', 'a']

# tup[0] = 245
# print(tup) #TypeError: 'tuple' object does not support item assignment


print(tup.count('a')) #2 tane 'a' elminti var
print(tup.count('b')) #1 tane
print(tup.count(True)) #0 tane var

print(tup.index('c')) #2 index


