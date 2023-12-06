
def paratlan(lista):
    paratlanok=[]
    osszeg=0
    for i in range(len(lista)):
        if lista[i]%2==1:
            paratlanok.append(lista[i])
    for i in paratlanok:
        osszeg=osszeg+i
    return osszeg

def paros(lista):
    parosak=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            parosak.append(lista[i])
    MennyiParosVan=len(parosak)
    return MennyiParosVan

import random
szamok=[]
while len(szamok)<500:
    x=random.randint(10000,99999)
    if x not in szamok:
        szamok.append(x)
MennyiParosVan=paros(szamok)
MennyiParatlanokOsszege=paratlan(szamok)
#ki iratás
print("Ennyi páros szám van:",MennyiParosVan)
print("Ennyi páratlan számok összege:",MennyiParatlanokOsszege)
#felek számolása
elsoFel=szamok[:249]

masodikFel=szamok[249:]
#eredményeik
elsoFelOsszeg=0

masodikFelOsszeg=0
#ciklusok
for i in elsoFel:
    elsoFelOsszeg=elsoFelOsszeg+i
    
for i in masodikFel:
    masodikFelOsszeg=masodikFelOsszeg+i
    
if masodikFelOsszeg<elsoFelOsszeg:
    print("Az első fél összege nagyobb mert az:",elsoFelOsszeg, "A második fel összege csak:",masodikFelOsszeg)
else:
    print("Az második fél összege nagyobb mert az:",masodikFelOsszeg, "A első fél összege csak:",elsoFelOsszeg)
#kezdő jegyes listák
EgyesselKezdodoSzamok=[]
KetesselKezdodoSzamok=[]
HarmassalKezdodoSzamok=[]
NegyesselKezdodoSzamok=[]
OtosselKezdodoSzamok=[]
HatossalKezdodoSzamok=[]
HetesselKezdodoSzamok=[]
NyolcassalKezdodoSzamok=[]
KilencesselKezdodoSzamok=[]
KezdoSzamok=['1','2','3','4','5','6','7','8','9']
for i in szamok:
    if str(i).startswith(KezdoSzamok[0]):
        EgyesselKezdodoSzamok.append(i)
          
for i in szamok:
    if str(i).startswith(KezdoSzamok[1]):
        KetesselKezdodoSzamok.append(i)
          
for i in szamok:
    if str(i).startswith(KezdoSzamok[2]):
        HarmassalKezdodoSzamok.append(i)
          
for i in szamok:
    if str(i).startswith(KezdoSzamok[3]):
        NegyesselKezdodoSzamok.append(i)
          
for i in szamok:
    if str(i).startswith(KezdoSzamok[4]):
        OtosselKezdodoSzamok.append(i)
          
for i in szamok:
    if str(i).startswith(KezdoSzamok[5]):
        HatossalKezdodoSzamok.append(i)
          
for i in szamok:
    if str(i).startswith(KezdoSzamok[6]):
        HetesselKezdodoSzamok.append(i)
          
for i in szamok:
    if str(i).startswith(KezdoSzamok[7]):
        NyolcassalKezdodoSzamok.append(i)
          
for i in szamok:
    if str(i).startswith(KezdoSzamok[8]):
        KilencesselKezdodoSzamok.append(i)
#mennyi olyan szamvan
EgyesSzamok=len(EgyesselKezdodoSzamok)
KettesSzamok=len(KetesselKezdodoSzamok)
HarmasSzamok=len(HarmassalKezdodoSzamok)
NegyesSzamok=len(NegyesselKezdodoSzamok)
OtosSzamok=len(OtosselKezdodoSzamok)
HatosSzamok=len(HatossalKezdodoSzamok)
HetesSzamok=len(HetesselKezdodoSzamok)
NyolcasSzamok=len(NyolcassalKezdodoSzamok)
KilencesSzamok=len(KilencesselKezdodoSzamok)
print("Ennyi 1essel kezdődő szám van:",EgyesSzamok)
print("Ennyi 2essel kezdődő szám van:",KettesSzamok)
print("Ennyi 3essel kezdődő szám van:",HarmasSzamok)
print("Ennyi 4essel kezdődő szám van:",NegyesSzamok)
print("Ennyi 5essel kezdődő szám van:",OtosSzamok)
print("Ennyi 6essel kezdődő szám van:",HatosSzamok)
print("Ennyi 7essel kezdődő szám van:",HetesSzamok)
print("Ennyi 8essel kezdődő szám van:",NyolcasSzamok)
print("Ennyi 9essel kezdődő szám van:",KilencesSzamok)

          

