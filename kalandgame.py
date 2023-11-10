def menu(lista):
    for i,elem in enumerate(lista):
        print("{}: {}".format(i+1,elem))

    valasztas=0    
    while (valasztas<1 or valasztas>len(lista)) and valasztas!=69:
        try:
            valasztas=int(input("Válassz:  "))
        except:
                    pass

    return valasztas-1

lista=["előre", "hátra", "jobbra", "balra"]

#valasz=menu(lista)
#print(valasz,lista[valasz])

tortenet=[
        [
            1,#szálId
            "Reggel felébredtem. Mit tegyek?",#szöveg
            ["fogmosás","Reggeli","Öltözés"],#választások
            [2,3,4] #hova ugorjon
        ],
        [
            2,#szálId
            "Elmegyek fogat mosni. Sikálom rendesen ahogy kell!",#szöveg
            ["fogmosás","Reggeli","Öltözés"],#választások
            [2,3,4] #hova ugorjon
        ],
        [
            3,#szálId
            "Kellene valamit enni! Anya csinált valamit? Nézzük meg!",#szöveg
            ["fogmosás","Reggeli","Öltözés"],#választások
            [2,3,4] #hova ugorjon
        ],
        [
            4,#szálId
            "Kisséhűvösvan, Kellene valami ruha! \nFelveszek egy nadrágot, meg egy pólót",#szöveg
            ["fogmosás","Reggeli","Öltözés", "66-os parancs"],#választások
            [2,3,4,66] #hova ugorjon
        ],
        [
            66,#szálId
            "végemindennek",
            [], #választások
            [] #hova ugorjon
        ]
    ]
SzalId=1
while True:
    temp=[]
    for e in tortenet:
        temp.append(e[0])
    #másként
    temp=[e[0] for e in tortenet]
    szalIndex=temp.index(SzalId)

    print(tortenet[szalIndex][1])
    
    if tortenet [szalIndex][2] == []:
        break

    menupont=menu(tortenet[szalIndex][2])

    if menupont == 68:
        break
    SzalId=tortenet[szalIndex][3][menupont]
print ("the end")
