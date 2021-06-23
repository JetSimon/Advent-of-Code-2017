arr = [0]*2018
pos = 0
steps = 3

for n in range(1,2018):
    pos += steps
    arr.insert(pos+1,n)
    pos = n

print(arr)
print( arr[arr.index(2017) + 1] )