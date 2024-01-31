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
BetuSzinek=["Blue",hatter,hatter,"Blue","Blue","Blue","Blue"]
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
#print(B2,E2,C2,N2,E3)

Bence=[[20, 100, 130, 100, 130, 150, 180, 150, 180, 220, 20, 220, 20, 100],
[47.5, 115, 102.5, 115, 102.5, 130, 47.5, 130, 47.5, 115], 
[47.5, 185, 140, 185, 140, 200, 47.5, 200, 47.5, 185],
[190.0, 100.0, 289.0, 100.0, 289.0, 127.0, 221.5, 127.0, 221.5, 154.0, 289.0, 154.0, 289.0, 181.0, 221.5, 181.0, 221.5, 208.0, 289.0, 208.0, 289.0, 235.0, 221.5, 235.0, 190.0, 235.0, 190.0, 100.0],
[440, 110, 550, 110, 550, 140, 465, 140, 465, 200, 550, 200, 550, 230, 440, 230, 440, 110],
[331.5, 99.0, 331.5, 236.99999999999997, 352.19999999999993, 236.99999999999997, 352.19999999999993, 161.1, 379.79999999999995, 236.99999999999997, 400.5, 236.99999999999997, 400.5, 99.0, 379.79999999999995, 99.0, 379.79999999999995, 161.1, 352.19999999999993, 99.0, 331.5, 99.0],
[580.0, 100.0, 679.0, 100.0, 679.0, 127.0, 611.5, 127.0, 611.5, 154.0, 679.0, 154.0, 679.0, 181.0, 611.5, 181.0, 611.5, 208.0, 679.0, 208.0, 679.0, 235.0, 611.5, 235.0, 580.0, 235.0, 580.0, 100.0]]
'''for e in B2:
    canvas.create_line(e,width=5,fill="blue")
for e in B:
    canvas.create_line(e,width=5,fill="red")'''
xTengely=0.5
yTengely=0.5

while True:
    canvas.delete("all")
    #Bence=transzformaciok.forgat(Bence,0.01)
    magassag=win.winfo_height()
    hossz=win.winfo_width()
    xek=[]
    yok=[]
    for elem in Bence:
        for i in range(len(elem)):
            if i%2==0:
                xek.append(elem[i])
            else:
                yok.append(elem[i])
    #legnagyobb kordináták
    xMaximum=max(xek)
    yMaximum=max(yok)
    #legkisseb kordináták
    xMinimum=min(xek)
    yMinimum=min(yok)

    if yMaximum>magassag or yMaximum<0:
        yTengely*=-1
    if xMaximum>hossz or xMinimum<0:
        xTengely*=-1
    sBence=transzformaciok.eltol(Bence,xTengely,yTengely)
    for i,e in enumerate(Bence):
        d=canvas.create_polygon(e,width=2,fill=BetuSzinek[i], outline="red")

    win.winfo_height()
    win.winfo_width()

    win.update_idletasks()
    win.update()

