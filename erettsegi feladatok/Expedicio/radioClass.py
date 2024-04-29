class Uzenet():
	def __init__(self,sor1,sor2):
		self.nap=int(sor1.split(" ")[0])
		self.amator=int(sor1.split(" ")[1])

		self.uzenet=sor2
		self.szamkereso()
	def szamkereso(self):
		
		self.kifejlett=False
		self.kolyok=False
		szamok=self.uzenet.split(" ")[0].split("/")
		if len(szamok)==2:
			if szamok[0].isnumeric():
				self.kifejlett=szamok[0]
			if szamok[1].isnumeric():
				self.kolyok=szamok[1]
	def farkasKereso(self):
		return "farkas" in self.uzenet
	

class Nap:
	def __init__(self, nap):
		self.nap=nap
		self.uzenetek=[]
	
	def hozzaAd(self,uzenet):
		self.uzenetek.append(uzenet)

	def uzenetSzam(self):
		return len(self.uzenetek)
	
	#5. feladat
	def helyreallit(self):
		megfejtes=self.uzenetek[0].uzenet

		for i,egyBetu in enumerate(megfejtes):
			if egyBetu=="#":
				for egyUzenet in self.uzenetek:
					if egyUzenet.uzenet[i]!="#":
						megfejtes=megfejtes[:i]+egyUzenet.uzenet[i]+megfejtes[i+1:]
						break
		return megfejtes
	
	#6. feladat
	def szame(self,szo) -> bool:
		valasz=True
		for i in range(len(szo)):
			if szo[i]<'0' or szo[i]>'9':
				valasz=False
		return valasz

	def radioamator(self,szam):
		for egyUzenet in self.uzenetek:
			if szam==egyUzenet.amator:
				return egyUzenet
		return False
