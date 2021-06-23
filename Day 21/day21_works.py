sample = False
inp = open('input.txt','r')
lines = []
for line in inp:
    lines.append(line.strip())
cur = """.#./..#/###"""
book = {}

def to_grid(s):
    return list(map(list, s.split("/")))

# rot 90 deg
def rot(grid):
    n = len(grid)
    o = [[None]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            o[i][j] = grid[~j][i]
    return o

def flip(grid):
    return list(map(reversed, grid))

def to_str(s):
    return "/".join("".join(x) for x in s)

for line in lines:
    a, b = line.split(" => ")

    for rots in range(4):
        for flips in range(2):
            transformed = to_grid(a)
            for _ in range(rots):
                transformed = rot(transformed)
            for _ in range(flips):
                transformed = flip(transformed)
            book[to_str(transformed)] = b

def iteration(grid):
    n = len(grid)
    if n % 2 == 0:
        new_n = n // 2 * 3
        split = 2
        newsplit = 3
    else:
        new_n = n//3 * 4
        split = 3
        newsplit = 4

    out = [[None]*new_n for _ in range(new_n)]
    for i in range(0, n // split):
        for j in range(0, n // split):
            si = i * split
            sj = j * split
            g = [row[sj:sj+split] for row in grid[si:si+split]]
            s = to_str(g)
            assert(s in book)
            transf = to_grid(book[s])

            ei = i * newsplit
            ej = j * newsplit
            for a in range(newsplit):
                for b in range(newsplit):
                    out[ei+a][ej+b] = transf[a][b]

    return out

cur = to_grid(cur)

for _ in range(18 if not sample else 2):
    cur = iteration(cur)

print(to_str(cur).count("#"))