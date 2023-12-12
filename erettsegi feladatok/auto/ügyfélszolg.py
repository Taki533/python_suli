adatok=[]
f=open("hivas.txt")

for sor in f:
    temp=[]
    tempSor=sor.split(" ")
    for e in tempSor:
        temp.append(int(e))
    
    temp.append(temp[3]*60*60+temp[4]*60+temp[5]-temp[0]*60*60+temp[1]*60+temp[3])    
    adatok.append(temp)
f.close()
    
print(adatok)