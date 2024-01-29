from errno import E2BIG
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
E=[0,0,110,0,110,30,35,30,35,60,110,60,110,90,35,90,35,120,110,120,110,150,35,150,0,150,0,0]
N = [850,100,850,300,880,300,880,190,920,300,950,300,950,100,920,100,920,190,880,100,850,100]
C=[0,0,110,0,110,30,25,30,25,90,110,90,110,120,0,120,0,0]

hatter="#ffffff"
BetuSzinek=["Blue",hatter,hatter]
canvas.create_line(B[0],width=5,fill="blue")
canvas.create_line(B[1],width=5,fill="blue")
canvas.create_line(B[2],width=5,fill="blue")
'''for e in B:
    e=transzformaciok.eltol(e,100,100)
    e=transzformaciok.nagyit(e,1.5)
    e=transzformaciok.forgat(e,45)
    B2.append(e)'''
B2=transzformaciok.masol(B)
B2=transzformaciok.nagyit(B2,1)
B2=transzformaciok.eltol(B2,20,100)

E2=transzformaciok.masol(E)
E2=transzformaciok.nagyit(E2,0.9)
E2=transzformaciok.eltol(E2,190,100)

N2=transzformaciok.masol(N)
N2=transzformaciok.nagyit(N2,0.69)
N2=transzformaciok.eltol(N2,-255,30)


C2=transzformaciok.masol(C)
C2=transzformaciok.eltol(C2,440,110)

E3=transzformaciok.masol(E)
E3=transzformaciok.nagyit(E3,0.9)
E3=transzformaciok.eltol(E3,580,100)



'''for e in B2:
    canvas.create_line(e,width=5,fill="blue")
for e in B:
    canvas.create_line(e,width=5,fill="red")'''
canvas.create_line(E,width=5,fill="red")
while True:
    canvas.delete("all")
    canvas.create_line(E2,width=5,fill="red")
    canvas.create_line(N2,width=5,fill="red")
    canvas.create_line(C2,width=5,fill="red")
    canvas.create_line(E3,width=5,fill="red")
    #B2=transzformaciok.forgat(B2,0.01)
    for i,e in enumerate(B2):
        d=canvas.create_polygon(e,width=2,fill=BetuSzinek[i], outline="red")
    
    win.update_idletasks()
    win.update()