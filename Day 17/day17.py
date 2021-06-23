arr = [0]
pos = 0
steps = 394

""" for n in range(1,50000000):
    pos += steps
    pos = pos % len(arr)
    i = pos + 1
    arr.insert(i,n)
    pos = i
    per = (n / 50000000) * 100
    print( arr[arr.index(0) + 1] )
#print(arr) """

steps = 394
# Part 2
curl = 1
pos = 0
out = 0
for i in range(50000000):
    to_ins = i+1
    new = (pos + steps) % curl
    new += 1
    if new == 1:
        out = to_ins
    pos = new
    curl += 1
print(out)