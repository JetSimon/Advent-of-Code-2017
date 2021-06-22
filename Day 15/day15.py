def generate(last, factor, div):
    return (last * factor) % div

def last16(n):
    l = len(n)
    return n[l-16:l]

def judge(a, b):
    a = last16(bin(a))
    b = last16(bin(b))

    return a == b

def fillStack(n, factor, mul,name="",fill=5000000):
    stack = []
    while len(stack) < fill:
        n = generate(n, factor, 2147483647)
        if n % mul:
            stack.append(n)
            print("stack",name,"at %", 100*(len(stack) / fill))
    return stack

a = 65
b = 8921

stacka = fillStack(a, 16807, 4,"A")
stackb = fillStack(b, 48271, 8,"B")

print("stack a has",len(stacka),"stack b has",len(stackb))

count = 0
pairs = 0

print("starting judgement")

for i in range(5000000):
    fa = stacka[i]
    fb = stackb[i]
    matching = judge(fa,fb)

    count = count + 1 if matching else count
    pairs += 1

    per = 100*(pairs/5000000)

    if(per % 1 == 0):
        print(per,"% complete")

print("FINAL COUNT:",count)