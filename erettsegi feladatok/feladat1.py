szavak=[]
print("1.feladat")
while True:
    szo=input("Kérek egy szót:")
    if szo=="":
        break
    else:
        szavak.append(szo)
print("szavakszáma: "+str(len(szavak)))
listafele=len(szavak)//2
print("A lista első fele:", end=" ")
for i in range(0,listafele):
    if i==listafele-1:
        print(szavak[i],end="\n")
    else:
        print(szavak[i], end="_")
        
