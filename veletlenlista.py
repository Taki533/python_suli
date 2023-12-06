import random
import math

def veletlen(mettol,meddig,lepes=1):
    darab=math.ceil((meddig-mettol)/lepes)
    eltolas=mettol
    
    szam=math.floor(random.random()*darab)*lepes+eltolas
    return szam

print(veletlen(10,20))   
lista=[]
r=veletlen(10,21)
for i in range(r):
    r2=veletlen(10,20)
    temp=[]
for i in range(r2):
    temp.append(veletlen(160,201))
    lista.append(temp)
print(lista)
