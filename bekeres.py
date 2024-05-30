szavak=[]

while True:
    szo=input("adj meg egy szot:")
    if szo=="":
        break
    elif len(szo)<=10:
        szavak.append(szo)
    else:
        szo=input("adj meg egy szot:")
print(szavak[-1])

for szo in szavak:
    if szo==szavak[-1]:
        pass
    elif szo==szavak[-2]:
        print(szo,end="\n")
    else:
        for i in range(1,len(szavak)):
            print(szavak[i]+" - ",end=" ")