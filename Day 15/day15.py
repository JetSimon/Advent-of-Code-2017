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
        if a % mul:
            stack.append(a)
            print("stack",name,"at %", 100*(len(stack) / fill))
    return stack

a = 65
b = 8921

stacka = fillStack(a, 16807, 4,"A")
stackb = fillStack(b, 48271, 8,"B")






count = 0
pairs = 0
while len(stacka) > 0 and len(stackb) > 0:
    fa = stacka.pop(0)
    fb = stackb.pop(0)
    matching = judge(fa,fb)

    count = count + 1 if matching else count
    pairs += 1

    per = 100*(pairs/5000000)
    if(per % 1 == 0):
        print(per,"% complete")

    if pairs == 5000000:
        running = False

print("FINAL COUNT:",count)