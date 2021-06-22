from math import sqrt

def getInput():
    out = []
    f = open('input.txt', 'r')
    for line in f:
        out += line.split(",")
    return out

steps = getInput()
x = 0
y = 0

best = 0

for step in steps:
    if step == "n":
        y+=1
    elif step == "s":
        y-=1
    elif step == "ne":
        x+=0.5
        y+=0.5
    elif step == "se":
        x+=0.5
        y-=0.5
    elif step == "nw":
        x-=0.5
        y+=0.5
    elif step == "sw":
        x-=0.5
        y-=0.5
    if abs(x)+abs(y) > best:
        best = abs(x)+abs(y)

print(x,y)

print(abs(x)+abs(y))

print("best: ", best)