from math import degrees, sin, cos, acos, asin, tan, atan,atan2,pi

class Node():
    def __init__(self,state):
        self.state = state
    def toggle(self):
        if self.state == "clean":
            self.state = "weak"
        elif self.state == "weak":
            self.state = "infected"
        elif self.state == "infected":
            self.state = "flagged"
        elif self.state == "flagged":
            self.state = "clean"


def readInput():
    loX = 0
    hiX = None
    loY = 0
    hiY = None
    out = {}
    y = 0
    x = 0
    f = open('input.txt','r')
    for line in f:
        x = 0
        for p in line.strip():
            state = "infected" if p == "#" else "clean"
            out[(x,y)] = Node(state)
            x += 1
            if loX == None or x < loX:
                loX = x

            if loY == None or y < loY:
                loY = y

            if hiX == None or x > hiX:
                hiX = x

            if hiY == None or y > hiY:
                hiY = y
        y += 1



    return out, (x-1) / 2, (y-1) / 2, loX, hiX, loY, hiY



def turn(dx,dy, da):
    angle = atan2( dy,dx );
    angle += da
    return int(cos(angle)), int(sin(angle))


map, x, y, loX, hiX, loY, hiY = readInput()

infected = 0

dx,dy = 0,-1


print("starting at",x,y)

bursts = 10000000

for burst in range(bursts):

    per = (burst/bursts) * 100
    if per % 1 == 0:
        print(per,"% done")

    #print("pos",x,y)
    if (x,y) not in map:
        #print(burst,": ",x,y,"not in map, adding..")
        map[(x,y)] = Node("clean")

    if map[(x,y)].state == "infected":
        dx, dy = turn(dx, dy, -pi/2)
    elif map[(x,y)].state == "clean":
        dx, dy = turn(dx, dy, pi/2)
    elif map[(x,y)].state == "weak":
        dx, dy = dx, dy
    elif map[(x,y)].state == "flagged":
        dx, dy = turn(dx, dy, pi)
    
    map[(x,y)].toggle()

    if map[(x,y)].state == "infected":
        infected += 1

    x -= dx
    y += dy

    if loX == None or x < loX:
        loX = x

    if loY == None or y < loY:
        loY = y

    if hiX == None or x > hiX:
        hiX = x

    if hiY == None or y > hiY:
        hiY = y
    #print(dx,dy)
    
print("l/hX",loX,hiY,"l/hY",loY,hiY)
print(infected,"infected!")
print("virus at ",x,y)

""" for i in range(int(loY), int(hiY)+1):
    row = []
    for j in range(int(loX), int(hiX)+1):
        c = "."
        if (j,i) in map:
            c = "#" if map[(j,i)] == True else "."
        
        if y == i and x == j:
            c = "@"
        
        if j == 0 and i == 0:
            c = "0"

        row.append(c)
    print(row)  """
