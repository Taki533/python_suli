#5ös lottó 5 számot sorsolnak benne 1-90ig
#6os lottő 1-45ig 6számot kell megtenni
#skandináv lottó 1-35-ig 7 számot kell megtenni
#totó 1 hazai 2 vendég x-döntetlen

Jatekok=["ötöslotto", "hatoslotto", "skandinavlotto", "toto"]

print("|========================Választások========================|")

for i,elem in enumerate(Jatekok):
    print("\t"+str(i+1)+":",elem)

print("\t0: Kilépés")

JatekId="alma"
while JatekId=="alma" or JatekId not in range(len(Jatekok)+1):
    try:
        JatekId=int(input("Válassz "))
        if JatekId not in range(len(Jatekok)+1):
           raise 
    except:
        print("válassz a listából")
print(|========================Eredmény========================|)
if  JatekId==1:
    import random
    randomlist = []
    while len(randomlist)<5:
        n = random.randint(1,91)
        if n not in randomlist:
            randomlist.append(n)
print(randomlist)

if JatekId==2
    import random
    randomlist2 = []
    while len (randomlist2)<6:
        n = random.randint(1,46)
        if n not in randomlist:
            randomlist2.append(n)
print(randomlist2)

if JatekId==3
    import random
    randomlist3 = []
    while len (randomlist3)<7:
        n = random.randint(1,36)
        if n not in randomlist:
            randomlist3.append(n)
print(randomlist3)

if JatekId==4
    import random
    randomlist4 = []
    while len (randomlist4)<14:
        n = random.randint()
        if n not in randomlist:
            randomlist2.append(n)
print(randomlist2)



