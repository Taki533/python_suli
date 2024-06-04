sorok=input("adja meg hány sor legyen")
if sorok.isnumeric():
    sorok=int(sorok)
    
oszlopok=input("Adja meg hány oszlop legyen")
if oszlopok.isnumeric():
    oszlopok=int(oszlopok)

kar=input("Kérek pontosan 1 karatert: ")

while len(kar)!=1:
    print("Nem megfelelő méret!")
    kar=input("Kérek pontosan 1 karatert: ")
oszlopSzam=0
while oszlopSzam!=oszlopok:
     oszlopSzam+=1
     print(kar*sorok)