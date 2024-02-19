#Egyszerű pong játék
#Start: 2024.01.31
#Takács Bence


from tkinter import *
import random

def rajz():
    
    labdaPos[0]+=labdaSpeed[0]
    labdaPos[1]+=labdaSpeed[1]
    szelesseg=win.winfo_width()
    magassag=win.winfo_height()
    if labdaPos[0]+labdaSize>=szelesseg or labdaPos[0]<0:
        labdaSpeed[0]*=-1
        #labdaColor=randomColor()
    elif labdaPos[1]+labdaSize>magassag or labdaPos[1]<0:
        labdaSpeed[1]*=-1
        #labdaColor=randomColor()

    labdaLista.append(canvas.create_oval(labdaPos[0],labdaPos[1],labdaPos[0]+labdaSize,labdaPos[1]+labdaSize, fill=labdaColor, outline=""))
    if len(labdaLista)==labdaListaHossz:
        canvas.delete(labdaLista[0])
        labdaLista.pop(0)
    win.after(jatekSpeed,rajz)
def randomColor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return ("#"+hex(r)[-2:]+hex(g)[-2:]+hex(b)[-2:]).replace("x","0")

def atmenetColor(red, green, blue):
    red+=5
    if red>255:
        red-=255
        green+=5
    if green>255:
        green-=255
        blue+=5
    if blue>255:
        blue-=255
    
    return ("#"+hex(red)[-2:]+hex(green)[-2:]+hex(blue)[-2:]).replace("x","0"),red,green,blue
#ablak létrehozása
win=Tk()

jatekHatter="lightgray"
jatekSpeed=5

#ablak mérete
win.geometry("1000x600")

win.title("Pong")

#canvas létrehozás
canvas=Canvas(win, width=600, height=600, bg=jatekHatter)

#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)


labdaSpeed=[5,5.25]
labdaPos=[0,0]
labdaSize=50

labdaColor="green"

labdaLista=[]
labdaListaHossz=3
red,green,blue=0,0,0

win.after(jatekSpeed,rajz)
win.mainloop()


while True:
    #labdaColor,red,green,blue=atmenetColor(red,green,blue)
    rajz()
    canvas.update()

