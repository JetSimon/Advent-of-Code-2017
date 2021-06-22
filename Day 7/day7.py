from statistics import mode

programs = {}

class Program:
    def __init__(self, name, weight, children=[]):
        self.name = name
        self.weight = weight
        self.children = children
    def childrenAsList(self):
        out = []
        for child in self.children:
            out.append(str(child.name) + " (" + str(child.weight) + ") , " + str(findChildrenWeight(child)))
        return out

inputFile = open('input.txt', 'r') 
for line in inputFile:
  stripped = line.rstrip()
  stripped = stripped.replace('\t', ' ')

  name = stripped.split("(")[0].strip()
  weight = int(stripped.split("(")[1].split(")")[0])
  programs[name] = Program(name, weight)


inputFile.seek(0,0)


for line in inputFile:
    stripped = line.rstrip()
    name = stripped.split("(")[0].strip()


    if("->" not in stripped):
        continue

    childrenRaw = stripped.split("->")[1].strip().split(",")
    children = []
    for child in childrenRaw:
        child = child.strip()
        children.append(programs[child])
    programs[name].children = children
inputFile.close()

results = []
for name in programs:
    program = programs[name]
    for child in program.children:
        results.append(child.name)

def findChildrenWeight(program):
    w = program.weight
    for child in program.children:
        w += findChildrenWeight(child)
    return w

def findOddOne(program):
    print(program.name, program.childrenAsList())
    children = program.children
    weights = {}
    for child in children:
        weights[child.name] = findChildrenWeight(child)
    norm = mode(weights.values())
    print("NORM: " + str(norm))
    for child in children:
        if findChildrenWeight(child) != norm:
            if(len(child.children) == 0):
                print(child.name + " has no children. has value of " + str(child.weight))
                return child.name
            return findOddOne(child)
bottomName = list(set(programs.keys()) - set(results))[0]

bottom = programs[bottomName]

print(findOddOne(bottom))