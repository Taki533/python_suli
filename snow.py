import random

maxWidth=120
maxHeight=100
flake=["*","❆","❄","❅","o"]
flakeOption=4
minFlakes=0
maxFlakes=5
rows=[]
for _ in range(maxHeight):
    actFlakes=random.randint(minFlakes,maxFlakes)

    actRow=" "*maxWidth

    flakes=random.sample(range(0,maxWidth),actFlakes)
    
    for i in flakes:
            usedFlake=random.randint(flakeOption)
            actRow=actRow[:i]+flake[usedFlake]+actRow[i+1:]
    rows.append(actRow)        


print("\n".join(rows))