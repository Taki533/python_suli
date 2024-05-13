from triatlonClass import *

f=open("triatlon.txt")
adatok= []
next(f)
for sor in f:
    adatok.append(triatlon(sor))
f.close()
indulok=len(adatok)
print("2. feladat: A versenyen {} induló volt".format(indulok))

for versenyzo in adatok:
    versenyzo.osszIdo()
nyertes=min(adatok, key=triatlon.osszIdo)

print("3. feladat: A verseny nyertese:")
print("neve: {}".format(nyertes.nev))
print("rajtszama: {}".format(nyertes.rajtSz))
nyertesIdo=nyertes.osszIdo()
print("összideje:",ido)
