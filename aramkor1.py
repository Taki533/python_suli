from tkinter import *
import math

class jel:
	x=0
	y=0
	meret=100
	
	szin="brown"
	def __init__(self,x,y,meret,canvas):
		self.x=x
		self.y=y
		self.meret=meret
		self.r=self.meret*0.06
		self.canvas=canvas
		self.rajz()
		self.bkp=[[self.x,self.y+self.meret*0.5],[self.x+self.meret,self.y+self.meret*0.5]]
		#bkp=bekötési pont

	def rajz(self,vonalak=[],korok=[]):
			self.canvas.create_rectangle(self.x,self.y,
			self.x+self.meret,self.y+self.meret,
			fill="blue")

			for egyvonal in vonalak:
				self.canvas.create_line(egyvonal, width=self.meret*0.03,fill=self.szin)
			for egyKor in korok:
				self.canvas.create_oval(egyKor, outline=self.szin,width=self.meret*0.03)  

	def vezetek(self,masik,sajatBKP=1, masikBKP=0):
		vonalak=[
                    [self.bkp[sajatBKP][0],self.bkp[sajatBKP][1],
                    masik.bkp[masikBKP][0],masik.bkp[masikBKP][1],
                    ]]
		for egyvonal in vonalak:
			self.canvas.create_line(egyvonal, width=self.meret*0.03,fill=self.szin)

class elem(jel):
		def rajz(self):
			vonalak=[
						[self.x,self.y+self.meret*0.5,
						self.x+self.meret*0.45,self.y+self.meret*0.5
						],
						[self.x+self.meret*0.45,self.y+self.meret*0.2,
						self.x+self.meret*0.45,self.y+self.meret*0.8
						],
						[self.x+self.meret*0.55,self.y+self.meret*0.4,
						self.x+self.meret*0.55,self.y+self.meret*0.6
						],
						[self.x+self.meret*0.55,self.y+self.meret*0.5,
						self.x+self.meret,self.y+self.meret*0.5
						]
					]
			jel.rajz(self,vonalak)

class kapcsolo(jel):
	def rajz(self):
		vonalak=[
                    [self.x,self.y+self.meret*0.5,
                    self.x+self.meret*0.333-self.r,self.y+self.meret*0.5
                    ],
                    [self.x+self.meret*0.333+self.r,self.y+self.meret*0.5,
                    self.x+self.meret*0.666-self.r,self.y+self.meret*0.3
                    ],
                    [self.x+self.meret*0.666+self.r,self.y+self.meret*0.5,
                    self.x+self.meret,self.y+self.meret*0.5
                    ]
				]
		korok=[
			[self.x+self.meret*0.333-self.r,self.y+self.meret*0.5-self.r,
			self.x+self.meret*0.333+self.r,self.y+self.meret*0.5+self.r],
			[self.x+self.meret*0.666-self.r,self.y+self.meret*0.5-self.r,
			self.x+self.meret*0.666+self.r,self.y+self.meret*0.5+self.r]
			]

		jel.rajz(self,vonalak,korok)

class lampa(jel):
	def rajz(self):
		dx=self.r/math.sqrt(2)
		self.r=self.meret*0.25
		vonalak=[
                    [self.x,self.y+self.meret*0.5,
                    self.x+self.meret*0.5-self.r,self.y+self.meret*0.5
                    ],
                    [self.x+self.meret*0.5-dx,self.y+self.meret*0.5-dx,
                    self.x+self.meret*0.5+dx,self.y+self.meret*0.5+dx
                    ],
					[self.x+self.meret*0.5+dx,self.y+self.meret*0.5-dx,
                    self.x+self.meret*0.5-dx,self.y+self.meret*0.5+dx
                    ],
					[self.x+self.meret*0.5+self.r,self.y+self.meret*0.5,
                    self.x+self.meret,self.y+self.meret*0.5]
				]
		korok=[
			[self.x+self.meret*0.5-self.r,self.y+self.meret*0.5-self.r,
			self.x+self.meret*0.5+self.r,self.y+self.meret*0.5+self.r],]
		
		jel.rajz(self,vonalak,korok)
		
class Ellenallas(jel):
	def rajz(self):
		vonalak=[
                    [self.x,self.y+self.meret*0.5,
                    self.x+self.meret*0.25,self.y+self.meret*0.5
                    ],
                    [self.x+self.meret*0.25,self.y+self.meret*0.4,
                    self.x+self.meret*0.25,self.y+self.meret*0.6,
					self.x+self.meret*0.75,self.y+self.meret*0.6,
                    self.x+self.meret*0.75,self.y+self.meret*0.4,
					self.x+self.meret*0.25,self.y+self.meret*0.4,
                    ],
					[self.x+self.meret*0.75,self.y+self.meret*0.5,
                    self.x+self.meret*1.0,self.y+self.meret*0.5
                    ]
				]
		jel.rajz(self,vonalak)

win=Tk()
win.geometry("600x620+100+20")
win.title("Áramkör 10b 02/2024")
canvas=Canvas(win,bg="white")
canvas.pack(fill=BOTH,expand=1)
elem1=elem(0,0,100,canvas)
elem1.rajz()
lampa1=lampa(300,0,100,canvas)
lampa1.rajz()
Ellenallas1=Ellenallas(0,400,100,canvas)
Ellenallas1.rajz
kapcsolo1=kapcsolo(0,300,100,canvas)
kapcsolo1.rajz()
elem1.vezetek(kapcsolo1)



win.mainloop()

#sziusss <3