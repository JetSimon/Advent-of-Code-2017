def printGrid(grid):
    for row in grid:
        print(row)

def loadInput():
    grid = []
    f = open('input.txt','r')
    for line in f:
        grid.append(list(line.replace('\n','')))
    return grid


def inGrid(y,x,grid):
    X = len(grid[0])
    Y = len(grid)
    return x >= 0 and x < X and y >= 0 and y < Y

def getStart(grid):
    for i in range(len(grid[0])):
        c = grid[0][i]
        if c == "|":
            return 0,i
    return -1

grid = loadInput()

letters = []
y,x = getStart(grid)
dx = 0
dy = 1
steps = 0
print(y,x)

printGrid(grid)

while True:
    steps += 1
    if(grid[y][x] not in [' ','+','|','-']):
        letters.append(grid[y][x])
        grid[y][x] = '+'

    #print("piece:",grid[y+dx][x+dy])
    if inGrid(y + dy, x + dx, grid) and grid[y+dy][x+dx] != " ":
        y = y + dy
        x = x + dx
    else:
        temp = dy
        dy = dx
        dx = temp
        if inGrid(y + dy, x + dx, grid) and grid[y+dy][x+dx] != " ":
            y = y + dy
            x = x + dx
        else:
            dy *= -1
            dx *= -1
            if inGrid(y + dy, x + dx, grid) and grid[y+dy][x+dx] != " ":
                y = y + dy
                x = x + dx
            else:
                print("stopped at",y,x)
                print("LETTERS","".join(letters))
                print("TOOK",steps,"STEPS")
                break
