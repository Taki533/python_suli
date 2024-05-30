from modul import *
osszeg=szam()
lista=[]
parameterek=[]
for i in range(0,osszeg):
    parameterek.append(100+i)
for szam in parameterek:
    lista.append(keplet(szam))
átlag=sum(lista)/len(lista)
print("lista átlaga: {0:.2f}".format(átlag))