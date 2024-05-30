import math
def keplet(szam):
    return (math.sqrt(42*szam**3+12)+(25*szam))/(2*(13-26))*4*(szam/6)
def szam():
    szamok=[]
    
    while len(szamok)<3:
        mostaniszam=len(szamok)+1
        szam=input(str(mostaniszam)+". szám:")
        szamok.append(int(szam))
        
    return sum(szamok)

