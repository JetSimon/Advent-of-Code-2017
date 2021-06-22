inputFile = open('input.txt', 'r') 
memory = []
seen = {}

for line in inputFile:
  stripped = line.rstrip()
  stripped = stripped.replace('\t', ' ')
  for n in stripped.split(" "):
      memory.append(int(n))

cycle = 0
while True:
    most = max(memory)
    for i in range(len(memory)):
        bank = memory[i]
        if bank == most:
            reserve = memory[i]
            memory[i] = 0
            pos = i + 1
            while reserve > 0:
                if pos >= len(memory):
                    pos = 0
                memory[pos] += 1
                reserve -= 1
                pos += 1
            break
    config = "".join(str(int) for int in memory)
    #print(config)
    if config in seen:
        print("time since: " + str(cycle - seen[config]))
        break
    else:
        seen[config] = cycle
        cycle += 1

print(cycle)