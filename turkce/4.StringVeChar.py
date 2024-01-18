strvar = "Python"
#         012345
print(strvar)
print(strvar[2]) #t
print(strvar[0:3]) #Pyt
print(strvar[:]) # Python
print(strvar[::2]) #Pto --yani iki basmaktan atliyor
print(strvar[::-1]) #nohtyP
print(strvar[::4]) #Po - 4taneden atliyor

print("----------------------------")

print(len(strvar)) #leng-index uzunluk

print(strvar + " ogren!") #Python ogren!

strvar = strvar + " ogren!"
print(strvar * 5) #Python ogren!Python ogren!Python ogren!Python ogren!Python ogren!


print(strvar.upper()) #PYTHON OGREN!
print(strvar.lower())  #python ogren!

print(strvar.split())  #['Python', 'ogren!']
print(strvar.split("o")) #['Pyth', 'n ', 'gren!']



