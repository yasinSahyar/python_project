
luku = 20
if luku > 20:
    print("Aabraham")
elif luku > 10:
    print("Bertta")
else:
    print("Ceillia")
print("David")                     ##Bertta , David

print("---------2-----------")

s = "J"
while s != "Jeee":
    print(s)
    s = s + "e"                  ## J ,Je, Jee

print("----------3---------")
for a in range(0,10,2):
    print(f"kierros: {a}")       ## 0,2,4,6,8

print("---------4--------------")
maat1 = []
maat2 = ["suomi","ruotsi","norja","tanska","islanti"]
maat3 = ["viro","latvia","liettua"]
maat2.extend(maat3)
maat1.extend(maat2)
maat1.append("puola")

print(maat1[1])              #ruotsi
if "viro" in maat2:
     print("juu")            #juu
     print("--------------")
else:
    print("ei")              #
    print("-------------")
if "viro" in maat1:
    print("joopajoo")         #joopajoo
    print("-------------")
else:
    print("eipäei")           #
print(maat1[-1])              #puola
