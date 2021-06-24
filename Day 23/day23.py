def loadInput():
    data = []
    f = open('input.txt','r')
    for line in f:
        data.append(line.strip())
    return data

class CPU:
    def __init__(self,id, instructions):
        self.id = id
        self.instructions = instructions
        self.data = {'a':1}
        self.q = []
        self.pos = 0
        self.partner = None
        self.timesSent = 0
        self.mulCount = 0
    
    def tick(self):
        #print(self.pos)
        if self.pos >= len(self.instructions):
            return False

        instruction = self.instructions[self.pos]
        command = instruction.split(" ")[0]
        X = instruction.split(" ")[1]
        X_reg = str(X)
        Y = instruction.split(" ")[2] if len(instruction.split(" ")) > 2 else None
        #print(data)
        if not X.lstrip("-").isdigit():
            if X not in self.data:
                self.data[X] = 0
            X = int(self.data[X])

        if type(Y) is str and not Y.lstrip("-").isdigit():
            #print(Y)
            if Y not in self.data:
                self.data[Y] = 0
            Y = int(self.data[Y])

        if command == "snd":
            self.timesSent += 1
            #print(self.id,"sending", X,"to",self.partner.id)
            self.partner.q.append(int(X))
        elif command == "set":
            self.data[X_reg] = int(Y)
        elif command == "add":
            self.data[X_reg] = int(X) + int(Y) 
        elif command == "sub":
            self.data[X_reg] = int(X) - int(Y) 
        elif command == "mul":
            self.mulCount += 1
            self.data[X_reg] = int(X) * int(Y)
        elif command == "mod":
            self.data[X_reg] = int(X) % int(Y)
        elif command == "rcv":
            if len(self.q) < 1:
                return False
            self.data[X_reg] = self.q.pop(0)
        elif command == "jnz":
            if int(X) != 0:
                self.pos += int(Y)
                return True
        self.pos += 1
        return True

A = CPU(0, loadInput())

while A.tick():
    print(A.data)

print(A.mulCount)



    