from tkinter import *
class jel:
	x=0
	y=0
	meret=100
	r=meret*0.06
	szin="brown"
	def __init__(self,x,y,meret,canvas):
		self.x=x
		self.y=y
		self.meret=meret
		self.canvas=canvas
		self.rajz()

		def rajz(self,vonalak=[]):
			self.canvas.create_rectangle(self.x,self.y,
			self.x+self.meret,self.y+self.meret,
			fill="blue")

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
                    [self.x+self.meret*0.333+r,self.y+self.meret*0.5,
                    self.x+self.meret*0.666-self.r,self.y+self.meret*0.3
                    ],
                    [self.x+self.meret*0.666+self.r,self.y+self.meret*0.5,
                    self.x+self.meret,self.y+self.meret*0.5
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

kapcsolo1=kapcsolo(0,300,100,canvas)
kapcsolo1.rajz()




win.mainloop()

#sziusss <3