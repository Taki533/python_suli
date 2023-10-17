lista=[]
bekeres="10"
while bekeres!=0 :
    bekeres=int(input("adj meg egy számot: "))
    lista.append(bekeres)
    
lista.pop()

print(lista)


paros=[]

for szam in lista:
    if szam%2==0:
        paros.append(szam)

print(paros)


paros=[]

for szam in lista:
    if szam//2*2==szam:
        paros.append(szam)

print(paros)
