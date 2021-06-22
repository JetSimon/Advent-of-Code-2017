instructions = []

inputFile = open('input.txt', 'r') 

for line in inputFile:
  stripped = line.rstrip()
  instructions.append(int(stripped))

size = len(instructions)


inputFile.close()
pos = 0
times = 0

while pos >= 0 and pos < size:
    amt = instructions[pos]

    if(instructions[pos] >= 3):
        instructions[pos] = instructions[pos] - 1
    else:
        instructions[pos] = instructions[pos] + 1
    times += 1
    pos += amt

print("Escaped in " + str(times) + " steps")
