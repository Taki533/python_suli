def ezredeles(szam):
    if len(str(szam))>4:
        szamSzama=0
        Cut=0
        UtsoSzamSzama=0
        for digit in str(szam):
            szamSzama+=1
            if szamSzama==3:
                print(digit+",", end="")
                szamSzama=0
            else: 
                print(digit, end="")
            
            
        print(end="\n")
cucc=ezredeles(1000000000000)