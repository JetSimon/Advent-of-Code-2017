from copy import deepcopy
class Wall:
    def __init__(self, depth):
        self.depth = depth
        self.pos = 0
        self.dy = 1
    
    def update(self):
        if self.pos + self.dy < 0 or self.pos + self.dy >= self.depth:
            self.dy *= -1
        self.pos += self.dy

def wallToConfig(walls):
    out = ""
    for wall in walls:
        out += (str(walls[wall].pos) + str(walls[wall].dy))
    return out

def getInput():
    out = {}
    biggest = 0
    f = open('input.txt','r')
    for line in f:
        pos = int(line.split(": ")[0])
        depth = int(line.split(": ")[1])
        if depth > biggest:
            biggest = depth
        out[pos] = Wall(depth)
        #print(pos, depth)
    return out, biggest


walls, biggest = getInput()
tried = {}
saved = deepcopy(walls)
#print(walls)
delay = 0
while True:
    delay += 1
    walls = deepcopy(saved)
    if delay % 100000 == 0:
        print(delay)

    for key in walls:
        wall = walls[key]
        wall.pos = 0

    #print("DELAY of", delay)
    sev = 0
    caught = False

    saved = deepcopy(walls)
    for key in walls:
        wall = walls[key]
        wall.update()
    
    config = wallToConfig(walls)

    tried[config] = True
            
    for pos in range(list(walls.keys())[-1] + 1):
        for key in walls:
            wall = walls[key]
            if(wall.pos == 0 and pos == key):
                #print("delay",delay,"caught at",pos)
                sev += key * wall.depth
                caught = True
        
        for key in walls:
            wall = walls[key]
            wall.update()
    
    if not caught:
        print("Won't Get Caught at ", delay)
        break
    #else:
        #print("Delay of ", delay, "results in", sev)