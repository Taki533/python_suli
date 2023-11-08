#ötbetűs szó kiiratása nem kell értelmes
#felváltva a magán és mássalhangzók a szóban
import random

Magan=["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű","b", "c", "cs", "d", "dz", "dzs", "f", "g", "gy", "h", "j", "k", "l", "m", "n", "ny", "p", "r", "s", "sz", "t", "ty", "v", "z", "zs"]
Szo=[]
while len(Szo)<5:
    Szo.append(random.choice(Magan))

if len(Szo)==5:
    print(*Szo, sep = '')
