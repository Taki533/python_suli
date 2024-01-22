
import math

#eltolás
def eltol(pontok,x,y):
    for i in range(0,len(pontok),2):
        pontok[i]+=x
        pontok[i+1]+=y
    return pontok

def nagyit(pontok,x,y=-1):
    if y==-1:
        for i in range(len(pontok)):
            pontok[i]*=x
    else:
        for i in range(len(pontok)):
            if i%2==0:
                pontok[i]*=x
            else:
                pontok[i]*=y
    return pontok


def forgatpont(x,y,szog):
    x2=math.cos(math.radians(szog))*x - math.sin(math.radians(szog))*y
    y2=math.sin(math.radians(szog))*x + math.cos(math.radians(szog))*y

    return x2,y2



def forgat(lista,szog,oY="",oX=""):
    
    #kX,kY=kozepszamol(fenyo2)
    if oX=="" and oY=="":
        oX,oY=kozepszamol(lista)
    
    elif oX=="" or oY=="":
        return lista
    
    lista=eltol(lista,-oX,-oY)

    for i in range(0, len(lista),2):
        lista[i],lista[i+1]=forgatpont(lista[i],lista[i+1],szog)

    lista=eltol(lista,oX,oY)

    return lista


def kozepszamol(lista):
    x=0
    y=0
    for i in range(len(lista)):
        if i%2==0:
            x+=lista[i]
        else:
            y+=lista[i]

    x=x/(len(lista)/2)
    y=y/len(lista)*2

    return x,y

if __name__ == '__main__':
    print("rendesen elindítva")
#else:
    #print("modulként betöltve")