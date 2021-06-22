from math import floor, isqrt

def solve1(n):
    dx = 1
    dy = 0
    sl = 1 
    x = 0
    y = 0
    sp = 0
    for k in range(n-1):
        x += dx
        y += dy
        sp += 1
        if(sp == sl):
            sp = 0
            buffer = dx
            dx = -dy
            dy = buffer
            if dy == 0:
                sl += 1

    return abs(x) + abs(y)

def solve2(n):
    pass #solved in unity

print(solve2(368078))