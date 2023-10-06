#mértékegység átváltó
#Takács Bence 2023.10.06
#Projekt Feladat

típusok=["hosszúság", "Terület", "Térfogat" , "Tömeg", "Űrmérték", "Űrméték + térfogat"]
egysegek=[["mm","cm","dm","m","km"],
            ["mm2", "cm2", "dm2", "m2", "km2"],
            ["mm3", "cm3", "dm3", "m3", "km3"],
         [],
         [],
         []]

valtok=[[10,10,10,1000,1],
        [100,100,100,1000000,1],
        [1000,1000,1000,1000000000,1],
        [],
        [],
        []]


print("|========================Átváltó========================|")

for i,elem in enumerate(típusok):
    print("\t"+str(i+1)+":",elem)

print("\t0: Kilépés")

típusId="alma"
while típusId=="alma" or típusId not in range(len(típusok)+1):
    try:
        típusId=int(input("Válassz "))
        if típusId not in range(len(típusok)+1):
           raise 
    except:
        print("válassz a listából")


print("|======================================================|")
típusId-=1
print("típus:" , típusok[típusId])
print("Mértékegységek")
print("Forrás")

for i,elem in enumerate(egysegek[típusId]):
    print("\t"+str(i+1)+":",elem)
print("\t0: Vissza")
egysegId="alma"
while egysegId=="alma" or egysegId not in range(len(egysegek[típusId])+1):
    try:
        egysegId=int(input("Válassz "))
        if egysegId not in range(len(egysegek[típusId])+1):
           raise 
    except:
        print("válassz a listából")
print("Cél")
for i,elem in enumerate(egysegek[típusId]):
    print("\t"+str(i+1)+":",elem)
print("\t0: Vissza")

egysegId2="alma"
while egysegId2=="alma" or egysegId2 not in range(len(egysegek[típusId])+1):
    try:
        egysegId2=int(input("Válassz "))
        if egysegId2 not in range(len(egysegek[típusId])+1):
           raise 
    except:
        print("válassz a listából")


szam=float(input("Mennyiség: "))
egysegId=-1
egysegId2=-1
if egysegId<egysegId2 :
    print(valtok[típusId][egysegId:egysegId2])
    szorzo=1
    for e in valtok[típusId][egysegId:egysegId2]:
        szorzo*=e
    eredmeny=szam/szorzo
else:
    print(valtok[típusId][egysegId2:egysegId])
    szorzo=1
    for e in valtok[típusId][egysegId2:egysegId]:
        szorzo*=e
    eredmeny=szam*szorzo


print(szam,egysegek[típusId] [egysegId], eredmeny, egysegek[típusId] [egysegId2])
