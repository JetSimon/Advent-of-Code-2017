from copy import deepcopy
comp = []

f = open('input.txt','r')
for line in f:
    line = line.strip()
    l = int(line.split("/")[0])
    r = int(line.split("/")[1])
    comp.append( (l,r) )

longest = [[0],[0]]

def getStrongest(comp, need, strength, bridge, longest,depth):

    if depth >= 36:
        result = strength if strength > longest[1][0] else longest[1][0]
        longest[1][0] = result

    if depth > longest[0][0]:
        longest[0][0] = longest[0][0] + 1


    if(len(comp) == 0):
        return strength

    biggest = strength

    for c in comp:
        if need[0] in c or need[1] in c:
            nextNeed = None
            
            if c[0] == need[0] or c[0] == need[1]:
                nextNeed = (c[1], c[1])
            else:
                nextNeed = (c[0],c[0])

            new = deepcopy(comp)
            new.remove(c)
            #bridge.append(c)
            att = getStrongest(new , nextNeed, strength + c[0] + c[1], deepcopy(bridge),longest,depth+1)
            if att > biggest:
                biggest = att
                #bigBridge[0] = bridge
    return biggest


print(getStrongest(deepcopy(comp), (0, 0), 0 ,[],longest,0))
print(longest)