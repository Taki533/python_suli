import random
import math

def veletlen(mettol,meddig,lepes=1):
    darab=math.ceil((meddig-mettol)/lepes)
    eltolas=mettol
    
    szam=math.floor(random.random()*darab)*lepes+eltolas
    return szam

print(veletlen(10,20))

szamok=[]

for i in range(100):
    szamok.append(veletlen(10,20))
print(szamok)
