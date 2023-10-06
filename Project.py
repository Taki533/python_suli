#mértékegység átváltó
#Takács Bence 2023.10.06
#Projekt Feladat

típusok=["hosszúság", "Terület", "Térfogat" , "Tömeg", "Űrmérték", "Űrméték + térfogat"]

print("========================Átváltó========================")
for elem in típusok:
    print(elem)

for i,elem in enumerate(típusok):
    print("\t"+str(i+1)+":",elem)

print("\t0: Kilépés")

típusId="alma"
while típusId=="alma" or típusId not in range(len(típusok)+1):
    try:
        típusId=int(input("Válassz"))
    except:
        print("válassz a listából")
