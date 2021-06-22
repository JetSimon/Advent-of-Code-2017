def readInput(path):
    out = ""
    f = open(path, 'r') 
    for line in f:
        out += line.strip()
    return out

def cleanUp(s):
    gar = 0
    out = ""
    skip = False
    for c in s:
        if not skip:
            if c == "!":
                skip = True
                gar += 1
            out += c
        else:
            skip = False
    return out, gar

def cleanUpAngle(s):
    gar = 0
    ignore = False
    out = ""
    for c in s:
        if(c == "<" and not ignore):
            ignore = True
        elif ignore == True and c == ">":
            ignore = False
        elif not ignore:
            out += c
        else:
            gar += 1
    return out, gar

def score(s):
    left = 0
    leftFound = 0
    right = 0
    toDel = []
    for i in range(len(s)):
        c = s[i]
        if c == "{":
            if left == right:
                leftFound = i
            left += 1
        elif c == "}":
            right += 1
            if left == right:
                toDel.append(leftFound)
                toDel.append(i)
    
    l = list(s)
    found = len(toDel) / 2

    out = ""
    for i in range(len(s)):
        if(i not in toDel):
            out += s[i]

    return out, not (out == s), found


stream = readInput("input.txt")
#print(stream)
#clean up !
stream, gar = cleanUp(stream)
#print(stream)
stream, inGar = cleanUpAngle(stream)

inGar -= gar

print(stream)

depth = 1
out = 0
changed = True

while changed:
    stream, changed, found = score(stream)
    print(stream, "FOUND " + str(found), found * depth)
    out += found * depth
    depth += 1

print("Score: " + str(out))

print("In garbage: " + str(inGar))