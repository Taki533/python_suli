szavak=[]
while True:
    szo=input("adj meg egy 6betűs szót:")
    if len(szo)!=6:
        print("A karakterek száma téves!")
        break
    elif len(szavak)>=1 and szo[-1]!=szavak[-1][0]:
        print("Nem illeszkedik")
        break
    elif len(szo)==6:
        szavak.append(szo)
lepesek=len(szavak)
if lepesek<2:
    print("kezdő")
elif lepesek>3 and lepesek<5:
    print("közepes")
elif lepesek>6:
    print("haladó")