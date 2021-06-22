inputRead = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
  stripped = line.rstrip()
  data = stripped.split(" ")
  inputRead.append(data)

inputFile.close()

def solve():
    sol = 0

    for p in inputRead:
        phrases = {}
        valid = True
        for word in p:
            word = "".join(sorted(word))
            if word not in phrases:
                phrases[word] = 1
            else:
                valid = False
                break
        sol += 1 if valid else 0

    return sol

print(solve())