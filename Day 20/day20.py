class Particle():
    def __init__(self,id, stats):
        self.id = id
        self.stats = stats
    
    def tick(self):
        self.stats['v'][0] += self.stats['a'][0]
        self.stats['v'][1] += self.stats['a'][1]
        self.stats['v'][2] += self.stats['a'][2]
        self.stats['p'][0] += self.stats['v'][0]
        self.stats['p'][1] += self.stats['v'][1]
        self.stats['p'][2] += self.stats['v'][2]
    
    def pos(self):
        out = ""
        for p in self.stats['p']:
            out+=(str(p))
        return out

def toInts(arr):
    for i in range(len(arr)):
        arr[i] = int(arr[i])



def getInput():
    out = []
    f = open('input.txt','r')
    id = 0
    for line in f:
        p = line.split("p=<")[1].split(">")[0].split(",")
        toInts(p)
        v = line.split("v=<")[1].split(">")[0].split(",")
        toInts(v)
        a = line.split("a=<")[1].split(">")[0].split(",")
        toInts(a)
        stats = {'a':a,'p':p,'v':v}
        out.append( Particle(id, stats) )
        id += 1
        
    return out

def magSum(arr):
    s = 0
    for n in arr:
        s+=abs(int(n))
    return s

def getLowest(arr, att):
    lowestVal = magSum(arr[0].stats[att])
    lowest = arr[0]
    for e in arr:
        v = magSum(e.stats[att])
        if v < lowestVal:
            lowestVal = v
            lowest = e
    return lowest

particles = getInput()

amt = 50000

for i in range(amt):

    pos = {}
    per = (i/amt) * 100

    if per % 1 == 0:
        print(per,"% done")

    for p in particles:
        p.tick()

        pz = p.pos()
        if pz in pos:
            pos[pz].append(p)
        else:
            pos[pz] = [p]
    
    for key in pos:
        if len(pos[key]) > 1:
            for p in pos[key]:
                particles.remove(p)

    


print(getLowest(particles, 'p').id)

print(len(particles),"left")