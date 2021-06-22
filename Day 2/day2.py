inputRead = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
  stripped = line.rstrip()
  stripped = stripped.replace('\t', ' ')
  stripped = stripped.split(" ")
  data = []
  for e in stripped:
      data.append(int(e))
  inputRead.append(data)

inputFile.close()

def solve():
    sol = 0

    for a in inputRead:
        for i in range(len(a)):
            for j in range(len(a)):
                q = a[i]
                p = a[j]
                if i !=j and q % p == 0:
                    sol += q / p

    return sol

print(solve())