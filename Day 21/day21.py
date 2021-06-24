def printGrid(arr):
    for row in arr:
        print(row)
    print("\n")

from copy import deepcopy
from typing import overload

def matches(a,b):
    if len(a) != len(b):
        return False

    for f in range(0,2):
        for fx in range(0,2):
            for sym in range(0,2):
                test = deepcopy(a)
                if f:
                    test = flip(test)
                if fx:
                    test = flipX(test)
                if sym:
                    test = symmetric(test)
                if same(test,b):
                    return True

    return False

def same(a,b):
    for y in range(len(a)):
        for x in range(len(a)):
            if a[y][x] != b[y][x]:
                return False
    return True

def symmetric(arr):
    out = deepcopy(arr)
    for y in range(len(arr)):
        for x in range(len(arr)):
            out[y][x] = arr[x][y]
    return out


def flip(arr):
    out = deepcopy(arr)
    for y in range(len(arr)):
        out[y] = arr[len(arr)-y-1]
    return out

def flipX(arr):
    out = deepcopy(arr)
    for y in range(len(arr)):
        for x in range(len(arr)):
            out[y][x] = arr[y][len(arr)-x-1]
    return out

def ruleToBlock(s):
    out = []
    for line in s.split("/"):
        out.append(list(line))
    return out

def blockToRule(arr):
    out = ""
    for line in arr:
        out += "".join(line) + "/"
    out = out[:len(out)-1]
    return out

def findRule(arr, rules):
    for rule in rules:
        block = ruleToBlock(rule)
        if matches(deepcopy(arr), block):
            #print("BLOCK", blockToRule(arr), "MATCHED WITH",rules[rule])
            return ruleToBlock(rules[rule])
    print("NO MATCH")
    return arr

def splitGrid(arr):
    l = len(arr)
    size = 2 if l % 2 == 0 else 3
    print("SIZE",size)
    out = []
    for y in range(0,len(arr),size):
        row = []
        for x in range(0,len(arr),size):
            chunk = arr[y:y+size]
            for i in range(len(chunk)):
                chunk[i] = chunk[i][x:x+size]
            row.append(chunk)
        out.append(row)
    #print("SPLIT INTO",(len(arr) / size) ** 2,"PIECES")
    return out

def joinGrid(arr):
    out = []
    i = 0
    j = 0
    gridSize = len(arr[0][0])
    #print(gridSize)
    current = arr[j][i]
    width = len(arr[0]) * gridSize
    height = len(arr) * gridSize
    
    for y in range(height):
        #print(i,j)
        row = []
        i = 0
        current = arr[j][i]
        if y % gridSize == 0 and y != 0:
            j += 1
            current = arr[j][i]
        for x in range(width):
            if x % gridSize == 0 and x != 0:
                i += 1
                current = arr[j][i]
            #print(y%gridSize, x%gridSize, j , i)
            row.append( current[y % gridSize][x % gridSize] )
        out.append(row)

    return out

def getRules():
    f = open('input.txt','r')
    out = {}
    for line in f:
        line = line.strip()
        a = line.split("=>")[0].strip()
        b = line.split("=>")[1].strip()
        out[a] = b
    return out

def getLit(arr):
    count = 0
    for row in arr:
        for e in row:
            if e == "#":
                count += 1
    return count


rules = getRules()
#print(rules)


out = [    ['.','#','.'],
            ['.','.','#'],
            ['#','#','#']]
print('STARTING POSITION')
printGrid(out)




for i in range(18):
    print("ITERATION",i+1)
    out = splitGrid( out )
    count = 0
    outOf = len(out) * len(out[0])
    for i in range (len(out)):
        for j in range (len(out[0])):
            count += 1
            per = (count / outOf) * 100
            if per % 1 == 0:
                print(per,"% done")
            out[i][j] = findRule(out[i][j], rules)
    out = joinGrid(out)
    #printGrid(out)

print(getLit(out))