from furdoClass import *
def idovissza(mp):
    ora=mp//(60*60)
    perc=mp%(60*60)//60
    masodp=mp%(60*60)%60
    if masodp in range(0,10):
        return str(ora)+":"+str(perc)+":"+"0"+str(masodp)
    else:
        return str(ora)+":"+str(perc)+":"+str(masodp)
#1. feladat
f=open("furdoadat.txt","r")
vendegek=[]
for sor in f:
    vendegek.append(Furdo(sor))
'''cica'''
f.close()

#2. feladat
print("2.feladat")
print("Az első vendég {}-kor lépett ki az öltözőből".format(vendegek[0].ido()))
utolso=vendegek[0]
for egyElem in vendegek:
    if not egyElem.belepett and egyElem.reszleg==0:
        utolso=egyElem
print("Az utolsó vendég {}-kor lépett ki az ötlözőből".format(utolso.ido()))

#3. feladat
darab=0
elozo=-1
temp=1
for egyElem in vendegek:
    if elozo==egyElem.vendeg:
        temp+=1
    else:
        if temp==4:
            darab+=1
        elozo=egyElem.vendeg
        temp=1
print("\n3. feladat")
print("A fürdőben {} vendég járt csak egy részlegen.".format(darab))
kezdoIdo=0
legtöbbIdo=0
LegtöbbIdoVendeg=0
for vendeg in vendegek:
    if vendeg.belepett and vendeg.reszleg==0:
        bentiIdo=vendeg.idoMp()-kezdoIdo
        if bentiIdo > legtöbbIdo:
            legtöbbIdo=bentiIdo
            LegtöbbIdoVendeg=vendeg.vendeg
    if not vendeg.belepett and vendeg.reszleg==0:
        kezdoIdo=vendeg.idoMp()
print("4. feladat:")
print("A legtöbb időt eltöltő vendég:")
print("{}. vendég {}".format(LegtöbbIdoVendeg,idovissza(legtöbbIdo)))
'''hf ido vissza nem 09 01 stb oldjuk meg hogy az legyen'''
print("<3")
stat=[0,0,0]

for Egyelem in vendegek:
    if Egyelem.reszleg==0 and not Egyelem.belepett:
        if Egyelem.ora < 9:
            stat[0]+=1
        elif Egyelem.ora < 16:
            stat[1]+=1
        else:
            stat[2]+=1
            
print("5.feladat")
print("6-9 óra között {} vendég\n9-16 óra között {} vendég\n16-20 óra között {} vendég".format(stat[0],stat[1],stat[2]))

szaunastat={}
temp=0
for Egyelem in vendegek:
    if Egyelem.reszleg==2:
        if Egyelem.belepett:
            temp=Egyelem.idoMp()
        else:
            #print(Egyelem)
            if egyElem.vendeg not in szaunastat.keys():
                szaunastat[Egyelem.vendeg]=0
            szaunastat[Egyelem.vendeg]+=Egyelem.idoMp()-temp
    f=open("szauna.txt","w")
    #print(szaunastat)
    for elem in szaunastat:
        #print(elem)
        f.write("{} {}\n".format(elem,idovissza(szaunastat[elem])))
    f.close()
    reszlegstat={}
    for egyElem in vendegek:
        if egyElem.belepett:
            if egyElem.reszleg not in reszlegstat:
                reszlegstat[egyElem.reszleg]=[]
            if egyElem.vendeg not in reszlegstat[egyElem.reszleg]:
                reszlegstat[egyElem.reszleg].append(egyElem.vendeg)
print("7. feladat")
reszlegLista=["Öltöző","Uszoda","Szaunák","Gyógyvizes medencék","Strand"]
for i in range(len(reszlegLista)):
    print("{}: {}".format(reszlegLista[i],len(reszlegstat[i])))