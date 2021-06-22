def connect(a, b):
    if(a not in b.connected):
        b.connected.append(a)
    if(b not in a.connected):
        a.connected.append(b)
    #print(a.id, " connected with ", b.id)

def processData():
    out = {}
    f = open('input.txt', 'r')

    for line in f:
        id = line.split("<->")[0].strip()
        out[id] = Line(id)
    
    f.seek(0,0)

    for line in f:
        a = line.split("<->")[0].strip()
        b_raw = line.split("<->")[1].strip().split(", ")
        for id in b_raw:
            connect(out[a],out[id])
        
    for line in out:
        print(out[line].connectedAsString())

    return out

class Line():
    def __init__(self, id):
        self.id = id
        self.connected = []
    
    def connectedTo(self, id):
        for c in self.connected:
            if c.id == id:
                return True
        return False
    
    def connectedAsString(self):
        out = []
        for c in self.connected:
            out.append(c.id)
        return self.id + ": " + str(out)

def isConnectedTo(line, id, visited):
    
    if line.connectedTo(id):
        return True
    if line.id in visited:
        #print(line.id, visited)
        return False

    visited[line.id] = True
    found = False

    for l in line.connected:
        if isConnectedTo(l, id, visited.copy()):
            found = True
    
    return found

inAlready = {}
groups = {}
lines = processData()

for id in lines:
    alr = False
    inGroup = ""
    for key in lines:
        line = lines[key]

        #print("trying",line.id)
        d = {}
        if isConnectedTo(line, id, d.copy()):
            if key in inAlready:
                #print(key,'already in')
                alr = True
                break
            #print(line.id,"is connected to",id)
            inGroup += key
            inAlready[key]=True
    #print("GROUP " + id + ":",inGroup)
    if alr:
        continue
    if inGroup not in groups:
        groups[inGroup] = True
        print(id, "is a group")

print(len(groups.keys()), "groups in total")

