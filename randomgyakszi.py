#egy 12 fős osztál minden évben kap 8-12 jegyet kap számoljuk ki az osztály átlagot
def átlag(lista,szamok):
    
    for i in lista[szamok]:
        temp=[]
        temp.append(i)
        Osztas=len(lista[szamok])
        for k in temp:
            oszzeg=0
            osszeg=osszeg+k
            atlag=osszeg/Osztas
    return atlag
import random

#12fő 8-12 jegy a jegy: magyaroszágon 1-5
jegyek=[]
for i in range(12):
    egyDiak=[]
    for k in range(random.randrange(8,13)):
        jegy=random.randrange(1,6)
        egyDiak.append(jegy)
    jegyek.append(egyDiak)

print(jegyek)
print(átlag(jegyek,1))