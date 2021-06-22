string = []

for i in range(256):
    string.append(i)

lengths = []
inp = "sadasd"
for c in inp:
    lengths.append(ord(c))
lengths += [17,31,73,47,23]

print("Lengths:",lengths)

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
    

pos = 0
skip = 0
for i in range(64):
    print("pos:", pos, "skip:", skip)
    for length in lengths:
        if(reverseFrom(string, pos, length)):
            pos += length + skip
            pos = pos % len(string)
            skip += 1
    
hash = ""
for i in range(0,256, 16):
    chunk = string[i:i+16]
    h = hex(xorChunk(chunk)).split("x")[1]
    hash += h

print(hash)