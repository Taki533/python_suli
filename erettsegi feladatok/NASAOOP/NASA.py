from NASAClass import *
f=open("NASAlog.txt")
adatok=[]
for egySor in f:
    adatok.append(megnyitas(egySor.strip()))
f.close
print("5. feladat: {}".format(len(adatok)))

osszeg=0
for egyAdat in adatok:
    osszeg+=egyAdat.ByteMeret()
print("6. Feladat: Válaszok összes mérete: {}".format(osszeg))