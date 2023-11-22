#Lista kiíratás függvénye
#KOCKADOBÁS
import random

def roll(minimum):
    return minimum<=random.randint(1,20)
#MENÜ KIÍRATÁS
def menu(lista,):
    for i, elem in enumerate(lista):
        print("{} - {}".format(i+1, elem))

    valasztas = 0

    while (valasztas<1 or valasztas>len(lista)) and valasztas != 69:
        try:
            valasztas = int(input("válassz egy számot a listából!"))
        except:
            pass

    return valasztas-1

#lista = ["Előre", "Hátra", "Jobbra", "Balra"]
#valasz = menu(lista);
#print(valasz, lista[valasz])


#Nyelv választás
nyelv=["Magyar", "English", "Deutsch", "Russian"]
nyelvId={"Magyar":"szovegHun","English":"szovegEng", "Deutsch":"szovegDEU","Russian":"szovegRu"}
print("Válassz nyelvet")
while True:
    nyelvValasztas=menu(nyelv)
    #print(nyelv[nyelvValasztas])
    if nyelv[nyelvValasztas] in nyelvId:
        break
    else:
        print("Sajnos ez a fordítás még nem készült el!")

if nyelvId[nyelv[nyelvValasztas]] == "szovegHun":
    import szovegHun as t
elif nyelvId[nyelv[nyelvValasztas]] == "szovegEng" :
    import szovegEng as t
elif nyelvId[nyelv[nyelvValasztas]] == "szovegDEU" :
    import szovegDEU as t
elif nyelvId[nyelv[nyelvValasztas]] == "szovegRu" :
    import szovegRu as t
bonusz=0
tortenet=[
        [
            1,#szál ID
            t.text["Megérkezel a kazamata bejáratához. Csikorogva kinyílik az ajtó és egy sötét, dohos folyosó fogad."], #szöveg szovehun fájlból választja ki a nyelvet
            [t.text["belépsz és gyújtasz egy fáklyát"], t.text["besétálsz a sötétbe"]], #választái lehetőségek
            [3,2] #hova ugorjon
        ],
        [
            2,#szál ID
            t.text["Túl hideg van, halálra fagytál!"], #szöveg
            [t.text["újrakezdés"], t.text["kilépés"]], #választái lehetőségek
            [1,66] #hova ugorjon
        ],
        [
            3,#szál ID
            t.text["Gyújtasz egy fáklyát. Balra van egy nyitott ajtó, de a fény nem hatol be. Jobbra egy zárt, rozoga ajtó."], #szöveg
            [t.text["Jobb oldali ajtó"], t.text["Bal oldali ajtó"]], #választái lehetőségek
            [4,5] #hova ugorjon
        ],
        [
            4,#szál ID
            t.text["Besétálsz a nyitott szobába, a fáklyád nem ér semmit, ezért nem látsz és belesétálsz egy medvecsapdába."], #szöveg
            [t.text["újrakezdés"], t.text["kilépés"]], #választái lehetőségek
            [1,66]#hova ugorjon
        ],
        [
            5,#szál ID
            t.text["Megpróbálod kinyitni az ajtó. Nincs zárva, ezért lassan csikorogva kinyílik. Egy kobold van a szobában."], #szöveg
            [t.text["harc! (könnyű)"], t.text["menekülés"]], #választái lehetőségek
            [7 if roll(12) else 7 if roll(12) else 8,6] #hova ugorjon
        ],
        [
            6,#szál ID
            t.text["Gyáván megfutamodtál. A játék véget ért!"], #szöveg
            [t.text["újrakezdés"], t.text["kilépés"]], #választái lehetőségek
            [1,66] #hova ugorjon
        ],
        #nyertél vesztettél
        [
            7,#szál ID
            t.text["Nagyobbat dobtál mint az ellenfél, ezért csúnyán megverted!"], #szöveg
            [t.text["kifosztod"], t.text["átvizsgálod a szobát"]], #választái lehetőségek
            [9,11] #hova ugorjon
        ],
        [
            8,#szál ID
            t.text["Kevesebbet dobtál mint az ellenfél, ezért csúnyán megvert! Meghaltál!"], #szöveg
            [t.text["újrakezdés"], t.text["kilépés"]], #választái lehetőségek
            [1,66] #hova ugorjon
        ],
        [
            9,#szál ID
            t.text["Átkutatod a koboldot. Találsz nála egy rozsdás kenőkést, és egy félig megevett zsíroskerenyeret. A rozsdás kenőkés szerencsét hoz!"], #szöveg
            [t.text["átvizsgálod a szobát"], t.text["visszamész a folysóra"]], #választái lehetőségek
            [11,10] #hova ugorjon
        ],
        [
            10,#szál ID
            t.text["A folysó továbbra is üres. Most megfigyeled a végét, és látod hogy nincs folytatása."], #szöveg
            [t.text["vissza a szobába"]], #választái lehetőségek
            [11] #hova ugorjon
        ],
        [
            11,#szál ID
            t.text["A szobát bevilágítja a fáklyád. Van bent egy asztal, és pár szék. Előtted és jobbról is egy ajtó van."], #szöveg
            [t.text["Előttem lévő ajtó kinyitása"], t.text["jobb oldali ajtó kinyitása"]], #választái lehetőségek
            [12,12] #hova ugorjon
        ],
        [
            12,#szál ID
            t.text["Odasétálsz az ajtóhoz, és szerencsédre nyitva van"], #szöveg
            [t.text["bemész"], t.text["másik ajtó megnézése"]], #választái lehetőségek
            [14,13] #hova ugorjon
        ],
        [
            13,#szál ID
            t.text["A jobb oldali ajtó zárva van. Lehetetlen kinyitni."], #szöveg
            [t.text["vissza a másikhoz"]], #választái lehetőségek
            [14] #hova ugorjon
        ],
        [
            14,#szál ID
            t.text["Besétálsz az ajtón, és látsz egy kijáratot, fény szűrődik onnan. De egy hatalmas ork állja az utad."], #szöveg
            [t.text["Harcolsz vele(nehéz)"],t.text["megpróbálod megkerülni"]], #választái lehetőségek
            [16 if roll(16-bonusz) else 16 if roll(16-bonusz) else 17,15] #hova ugorjon
        ],
        [
            15,#szál ID
            t.text["Megpróbáltál elfutni az ork mellett, és nagy szerencsédre sikerrel jártál és kijutottál a kazamatából"], #szöveg
            [t.text["játék újrakezdése"],t.text["kilépés"]], #választái lehetőségek
            [1,66] #hova ugorjon
        ],
        [
            16,#szál ID
            t.text["Nagyobbat dobtál mint az ellenfél, ezért legyőzted és végre kijutottál a kazamatából. Szép munka!"], #szöveg
            [t.text["játék újrakezdése"], t.text["kilépés"]], #választái lehetőségek
            [1,66] #hova ugorjon
        ],
        [
            17,#szál ID
            t.text["Kevesebbet dobtál mint az ellenfél, ezért csúnyán elfenekelt! Meghaltál!"], #szöveg
            [t.text["újrakezdés"], t.text["kilépés"]], #választái lehetőségek
            [1,66] #hova ugorjon
        ],
        [
            66,#szál ID
            t.text["Kiléptél!"], #szöveg
            [], #választái lehetőségek
            [] #hova ugorjon
        ]
    ]

szalId=1
while True:
    #temp=[]
    #for e in tortenet:
    #    temp.append(e[0])
    #másként listák ID kígyűjtése
    temp=[e[0] for e in tortenet]
    szalIndex=temp.index(szalId)

    print(tortenet[szalIndex][1])
    
    if tortenet[szalIndex][2]==[]:
        break

    menuPont = menu(tortenet[szalIndex][2])

    if menuPont == 68:
        break

    szalId=tortenet[szalIndex][3][menuPont]
        

print("The End")




