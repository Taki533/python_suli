#készítsünk egy listát a listában legyenek számok keressük meg a legnagyobbat, ezt tegyük fügvénnyel és a fügvény adja vissz melyik az a szám és holvan
def maxKeres(lista):
    maxIndex=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            maxIndex.append(i)
    
    return(maxIndex)
lista=[100,69,35,42,73,55,66,100,33,22,70,81,100]
maxIndex=maxKeres(lista)
print(maxIndex)
