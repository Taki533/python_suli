


f=open("bela.txt","w")

#f.write("1")

for i in range(100):
    f.write(str(i)+"\n")
f.close()

open("bela.txt","w").write("\n".join([str(i) for i in range(100)]))

f=open("bela.txt","r")

list=[]

for egySor in f:
    list.append(egySor.strip())
f.close()
print(list)

f=open("bela.txt","r")
list2=[ egySor.strip() for i in f.readlines()]