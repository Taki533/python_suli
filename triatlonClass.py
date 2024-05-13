class triatlon():
    def __init__(self,sor) -> None:
        vag=sor.strip().split(";")
        self.nev=vag[0]
        self.nem=vag[1]
        self.szulet=vag[2]
        self.uszas=vag[3]
        self.kerekpar=vag[4]
        self.futas=vag[5]
        self.rajtSz=vag[6]
    def osszIdo(self):
        return sum((int(t.split(":")[0]) * 3600 + int(t.split(":")[1]) * 60 + int(t.split(":")[2])) for t in [self.uszas, self.kerekpar, self.futas])
            
    
