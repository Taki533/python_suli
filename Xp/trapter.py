import math
a=0
while True:
    try: 
        a=(int(input("írd be az \"a\" oldal hosszát: "))) 
        break 
    except:
        print("adj meg egy számot")
b=0
while True:
    try: 
        b=(int(input("írd be az \"b\" oldal hosszát: "))) 
        break 
    except:
        print("adj meg egy számot")
c=0
while True:
    try: 
        c=(int(input("írd be az \"c\" oldal hosszát: "))) 
        break 
    except:
        print("adj meg egy számot")
d=0
while True:
    try: 
        d=(int(input("írd be az \"d\" oldal hosszát: "))) 
        break 
    except:
        print("adj meg egy számot")
        
T=(a+c)/(4*(a-c))*math.sqrt((a+b-c+d)*(a-b-c+d)*(a+b-c-d)*((-a)+b+c+d))
print(T)

#vagy

T2=(a+c)/(4*(a-c))*((a+b-c+d)*(a-b-c+d)*(a+b-c-d)*((-a)+b+c+d))**0.5
print(T2)
