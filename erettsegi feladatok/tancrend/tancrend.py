adatok=[]
f=open("erettsegi feladatok/tancrend/tancrend.txt")

for sor in f:
    adatok.append(sor.strip())
f.close()
print(adatok)