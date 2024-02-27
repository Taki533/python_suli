class Emlos():
	lab=4
	def __init__(self,suly):
		self.suly=suly
		
	def beszel(self):
		print("Emlős vagyok")


class Macska(Emlos):
	def __init__(self, suly, nev):
		super().__init__(suly)
		self.nev=nev
		self.suly=suly

	def beszel(self):
		print("Miauu")

class Birman(Emlos):
	def __init__(self, suly, nev, szin, szorhossz, kor, tipus):
		super().__init__(suly)
		self.nev=nev
		self.szin=szin
		self.szorhossz=szorhossz
		self.kor=kor
		self.tipus=tipus
	
	def tulajdon(self):
		print("Házikedvenced:")
		f=f"Tömeg: {self.suly} \nKinézet: {self.szin}, {self.szorhossz} szőrhossz \nKor: {self.kor} \nKaszt: {self.tipus} "
		print(f)

	def eltunt(self):
		felhivas=f"Eltűnt a {self.nev} névre hallgató {self.tipus} macskánk, {self.szin} színű és {self.szorhossz} hosszú szőre van. Ha látod kérlek telefonálj ezen a számon: 06205469981"
		print(felhivas)
		




emlos1=Emlos(50)
#emlos1.beszel()

macska1=Macska(50,"Adolf")
#macska1.beszel()
macska2=Birman(50,"Péter","szürke","közepes",4,"Birman")
macska2.eltunt()
macska2.tulajdon()

#MÁSIK MACSKA KÉSZÍTÉSE (1<) egy két függvény meg tulajdonság