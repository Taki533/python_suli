adatok=[]

f=open("NASAlog.txt")

for sor in f:
    adatok.append(sor.split("*"))
#for e in adatok:
    
f.close()