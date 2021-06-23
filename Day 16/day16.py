instructions = []
f = open('input.txt','r')
for line in f:
    instructions += line.split(",")

def spin(arr, l):
    return arr[len(arr)-l:len(arr)] + arr[:len(arr)-l]

def exchange(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partner(arr, a, b):
    i = arr.index(a)
    j = arr.index(b)
    exchange(arr, i, j)

arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
count = 0
start = "".join(arr)
first = True

#the steps loop at 24 and 1 billion % 24 = 16 so we can just run it 16 times for the same result
for i in range(16):
    first = False
    count += 1
    for inst in instructions:
        if inst[0] == "s":
            arr = spin(arr, int(inst[1:]))
        elif inst[0] == "x":
            exchange(arr, int(inst[1:].split("/")[0]), int(inst[1:].split("/")[1]))
        elif inst[0] == "p":
            partner(arr, inst[1:].split("/")[0], inst[1:].split("/")[1])
    

print("".join(arr))