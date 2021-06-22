lines = [x.rstrip().split(': ') for x in open('input.txt','r')]
delay = 1
while delay:
    s = 0
    for line in lines:
        line = [int(x) for x in line]
        sev = (delay + line[0]) % ((line[1] - 1) * 2)
        if not sev:
            s += line[0] * line[1]
            break
    else:
        print(delay)
        break
    delay += 1