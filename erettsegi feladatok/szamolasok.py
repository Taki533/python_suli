szamok=[]
szam=input("Adj meg egy számot:")
if szam!="0":
    szamok.append(int(szam))
while szam!="0":
    if szam=="0":
        pass
    else:
        szam=input("Adj meg egy számot:")
        szamok.append(int(szam))
    
negativ=[]
pozitiv=[]
for szam in szamok:
    if szam<0:
        negativ.append(szam)
    else:
        pozitiv.append(szam)
print(pozitiv, negativ)
negativSum=sum(negativ)
pozitivSum=sum(pozitiv)

if abs(negativSum)>pozitivSum:
    print("A negativ értékek összege messzeb van a nullától")
else:
    print("A pozitiv értékek összege messzeb van a nullától")

listafele=len(szamok)//2
for i in range(0,listafele):
    print(szamok[i], end=" ")
    if szamok[i]<0:
        pass