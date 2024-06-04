import math
def szamharmas():
    pontok=[]
    x=input("Adja meg az x kordinátát: ")
    y=input("Adja meg az y kordinátát: ")
    r=input("Adja meg a sugarat: ")
    pontok.append(int(x))
    pontok.append(int(y))
    pontok.append(int(r))
    return pontok
    
# r1: az első kör sugara
# r2: a második kör sugara
# d: a középpontok távolsága

# két kör érinti egymást, ha a sugaruk összege megegyezik a középpontjaik távolságával
# visszatérési értéke: logikai
def erint(r1,r2,d):
    temp=listaKeszit(r1,r2,d)
    return temp[0]+temp[1]==temp[2]

# két kör nem érinti és nem is metszi egymást, ha a sugaraik és távolságuk közül a két kisebb összege kisebb, mint a harmadik
# a körök lehetnek kívül, vagy belül is
# visszatérési értéke: logikai
def nemErint(r1,r2,d):
    temp=listaKeszit(r1,r2,d)
    return temp[0]+temp[1]<temp[2]

# két kör metszi egymást, ha a sugaraik és távolságuk közül a két kisebb összege nagyobb, mint a harmadik
# a körök lehetnek kívül, vagy belül is
# visszatérési értéke: logikai
def metsz(r1,r2,d):
    temp=listaKeszit(r1,r2,d)
    return temp[0]+temp[1]>temp[2]

# rendezi az adatokat, hogy megtudjuk melyik a leghosszabb
# visszatérési értéke: rendezett lista
def listaKeszit(r1,r2,d):
    temp=[r1,r2,d]
    temp.sort()
    return temp

def viszony(lista1,lista2):
    tav=math.sqrt(((lista1[0]-lista2[0])**2)+((lista1[1]+lista2[1])**2))
    if metsz(lista1[2],lista2[2],tav)==True:
        metszi=1
        return metszi
    if erint(lista1[2],lista2[2],tav)==True:
        erinti=1
        return erinti
    if nemErint(lista1[2],lista2[2],tav)==True:
        nemErinti=1
        return nemErinti