print("1. feladat")
szo=input("Kérek egy szöveget:")
szam=input("Kérek egy egész számot:")
while True:
    if szam.isnumeric()==True:
        szam=int(szam)
        break
    else:
        szam=input("Kérek egy egész számot:")

print(szo[szam-1]*szam)
