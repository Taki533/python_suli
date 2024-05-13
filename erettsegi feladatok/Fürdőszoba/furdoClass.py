class Furdo:
    def __init__(self,sor):
        vag=sor.split(" ")
        self.vendeg=int(vag[0])
        self.reszleg=int(vag[1])
        self.belepett=vag[2]=="0"
        self.ora=int(vag[3])
        self.perc=int(vag[4])
        self.masodperc=int(vag[5])
        
    def ido(self):
        return ":".join([str(self.ora),str(self.perc),str(self.masodperc)])
    def idoMp():
        return self.ora*60*60+self.perc*60+self.masodperc