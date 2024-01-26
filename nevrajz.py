import transzformaciok
from tkinter import *
win=Tk()

#ablak mérete
win.geometry("600x600")
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)
fenyo2=[200,0,
        0,100,
        150,100,
        0,200,
        150,200,
        0,300,
        150,300,
        150,400,
        250,400,
        250,300,
        400,300,
        250,200,
        400,200,
        250,100,
        400,100,
        200,0]
#canvas.create_line(fenyo2,width=5,fill="green")
#fenyo2Masolat=transzformaciok.eltol(fenyo2,100,100)
#canvas.create_line(fenyo2Masolat,width=5,fill="green")
B=[[0,0,110,0,110,50,160,50,160,120,0,120,0,0],#fenti lyuk
   [27.5,15,82.5,15,82.5,30,27.5,30,27.5,15],#also lyuk
   [27.5,85,120,85,120,100,27.5,100,27.5,85]]
hatter="#ffffff"
BetuSzinek=["Blue",hatter,hatter]
canvas.create_line(B[0],width=5,fill="blue")
canvas.create_line(B[1],width=5,fill="blue")
canvas.create_line(B[2],width=5,fill="blue")
B2=[]
'''for e in B:
    e=transzformaciok.eltol(e,100,100)
    e=transzformaciok.nagyit(e,1.5)
    e=transzformaciok.forgat(e,45)
    B2.append(e)'''
B2=transzformaciok.masol(B)
B2=transzformaciok.forgat(B2,-45)
B2=transzformaciok.nagyit(B2,1.2)
B2=transzformaciok.eltol(B2,100,100)



'''for e in B2:
    canvas.create_line(e,width=5,fill="blue")
for e in B:
    canvas.create_line(e,width=5,fill="red")'''

while True:
    canvas.delete("all")
    B2=transzformaciok.forgat(B2,0.01)
    for i,e in enumerate(B2):
        d=canvas.create_polygon(e,width=2,fill=BetuSzinek[i], outline="red")
    
    win.update_idletasks()
    win.update()