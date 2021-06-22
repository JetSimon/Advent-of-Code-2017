def getIslands(grid):
    count = 0
    for y in range(128):
        for x in range(128):
            if grid[y][x] == "1":
                flood(grid, y, x)
                count += 1
    return count

def flood(grid, y, x):

    if(y >= 128 or y < 0 or x < 0 or x >= 128):
        return

    if grid[y][x] == "1":
        grid[y][x] = "X"
        flood(grid, y + 1, x)
        flood(grid, y - 1, x)
        flood(grid, y, x + 1)
        flood(grid, y, x - 1)

def xorChunk(chunk):
    result = 0
    for e in chunk:
        result = result ^ e
    return result

def reverseFrom(arr, start, length):
    if length > len(arr):
        return False
    last = (start+length-1) % len(arr)
    visited = []
    #print("start", start, "last", last)
    for i in range(length):
        if((start + i) % len(arr) == (last - i) % len(arr)) or (last-i) % len(arr) in visited:
            break
        #print("swapping", (start+i) % len(arr), "(", arr[(start+i)% len(arr)], ") with", (last-i)% len(arr), "(", arr[(last-i)% len(arr)],")")
        temp = arr[(start+i) % len(arr)]
        arr[(start+i) % len(arr)] = arr[(last-i) % len(arr)]
        arr[(last-i) % len(arr)] = temp
        visited.append((start+i) % len(arr))
    return True
    
def knotHash(inp):
    string = []
    for i in range(256):
        string.append(i)
    lengths = []
    for c in inp:
        lengths.append(ord(c))
    lengths += [17,31,73,47,23]
    pos = 0
    skip = 0
    for i in range(64):
        #print("pos:", pos, "skip:", skip)
        for length in lengths:
            if(reverseFrom(string, pos, length)):
                pos += length + skip
                pos = pos % len(string)
                skip += 1
        
    hash = ""

    for i in range(0,256, 16):
        chunk = string[i:i+16]
        h = hex(xorChunk(chunk)).split("x")[1]
        if len(h) == 1:
            h = "0" + h
        hash += h
    return hash

def hexToBin(h):
    out = bin(int(h, 16)).split("b")[1]
    o =  ("0" * (4-len(out))) + out
    return o

key = "jxqlasbh"
raw = []
grid = []
used = 0

for n in range(128):
    raw.append(key + "-" + str(n))

for row in raw:
    out = []
    hash = knotHash(row)
    for c in hash:
        out += list(hexToBin(c))
    grid.append(out)

#print(grid)

#print(grid[3])

print("grid is", len(grid), "by", len(grid[0]))

print("ISLANDS:", getIslands(grid))

#for row in grid:
#    print(row)