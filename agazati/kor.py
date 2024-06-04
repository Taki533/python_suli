from kormodul import *
adatok=[]
while len(adatok)!=5:
    szamok=szamharmas()
    adatok.append(szamok)
metszesek=0
for i in range(1,len(adatok)+1):
    metszesVan=viszony(adatok[0],adatok[1])
    if metszesVan==True:
        metszesek+=1
if metszesek>0:
    print("Van, amelyik metszi az elsőt")
else:
    print("Nincs, olyan ami metszi az elsőt")
    