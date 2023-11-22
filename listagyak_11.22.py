#készítsünk egy listát a listában legyenek számok keressük meg a legnagyobbat, ezt tegyük fügvénnyel és a fügvény adja vissz melyik az a szám és holvan
def maxKeres(lista):
    maxIndex=0
    legnagyobb=lista[0]
    for i in range(len(lista)):
        if lista[i]>legnagyobb:
            legnagyobb=lista[i]
            maxIndex=i
    
    return(legnagyobb,maxIndex)
lista=[100,69,35,42,73,55,66,100,33,22,70,81,100]
legnagyobb,maxIndex=maxKeres(lista)
print(legnagyobb,maxIndex)
