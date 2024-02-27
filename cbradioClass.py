class Adatok:
    def __init__(self, sor):
        #6;0;2;Laci
        vag=sor.split(";")
        self.ora=int(vag[0])
        self.perc=int(vag[1])
        self.adas=int(vag[2])
        self.nev=(vag[3])
    def __str__(self):
        return "adat típus"
if __name__=="__main__":
    print("rendes")
    proba=Adatok("6;0;2;Laci")
    print(proba)