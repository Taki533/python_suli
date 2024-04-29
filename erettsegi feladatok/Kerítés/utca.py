class Telek:
    def __init__(self,sor) -> None:
        vag=sor.split(" ")
        self.oldal=int(vag[0])
        self.szelesseg=int(vag[1])
        self.szin=vag[2]
        self.hazszam=0
    


telkek=[]
f=open("kerites.txt")
parosParatlan=[0,-1]
for sor in f:
    telkek.append(Telek(sor))
    parosParatlan[telkek[-1].oldal]+=2
    telkek[-1].hazszam=parosParatlan[telkek[-1].oldal]    

f.close()

print("2. feladat")
print("Az eladott telkek száma: {}".format(len(telkek)))

print("3. feladat")

if telkek[-1].oldal==0:
    print("A páros oldalon adták el az utolsó telket")
else:
    print("A páratlan oldalon adták el az utolsó telket")
print("Az utolsó telek száma: {}".format(telkek[-1].hazszam))
oldalSzerint=[ [], [] ]