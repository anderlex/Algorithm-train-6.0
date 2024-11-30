def find_lighted(grid):
    x1, y1 = n, n
    x2, y2 = -1, -1
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '#':
                x1, y1 = min(x1, x), min(y1, y)
                x2, y2 = max(x2, x), max(y2, y)
    return x1, y1, x2, y2

def find_non_lighted(grid):
    x3, y3 = n, n
    x4, y4 = -1, -1
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '.':
                x3, y3 = min(x3, x), min(y3, y)
                x4, y4 = max(x4, x), max(y4, y)
    return x3, y3, x4, y4

def border_lighted(grid, x1, y1, x2, y2):
    a = []
    for x in range(x1, x2 + 1):
        a.append(grid[x][y1 : y2 + 1])
    return a

def is_I(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != '#': return False
    return True

def is_O(grid, x3, y3, x4, y4):
    if not (x1 < x3 <= x4 < x2 and y1 < y3 <= y4 < y2):
        return False
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i >= x3 and i <= x4 and j >= y3 and j <= y4:
                    if grid[i][j] != '.':
                        return False
                elif grid[i][j] != '#':
                    return False
        return True

def is_C(grid, x3, y3, x4, y4):
    if not (x1 < x3 <= x4 < x2 and y1 < y3 <= y4 and y4 == y2):
        return False
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i >= x3 and i <= x4 and j >= y3 and j <= y4:
                    if grid[i][j] != '.':
                        return False
                elif grid[i][j] != '#':
                    return False
        return True

def is_L(grid, x3, y3, x4, y4):
    if not (x1 == x3 and x3 <= x4 < x2 and y1 < y3 <= y4 and y4 == y2):
        return False
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i >= x3 and i <= x4 and j >= y3 and j <= y4:
                    if grid[i][j] != '.':
                        return False
                elif grid[i][j] != '#':
                    return False
        return True

def is_H(grid, x3, y3, x4, y4):
    x5, y5 = x3, y3
    x6, y6 = x5, y4
    while grid[x6][y6] == '.':
        x6 += 1
    x6 -= 1
    x3 = x4
    while grid[x3][y3] == '.':
        x3 -= 1
    x3 += 1
    if not (x1 == x5 and x5 <= x6 < x3 <= x4 and x4 == x2 and
            y1 < y3 and y3 == y5 and y5 <= y4 and y4 == y6 and y6 < y2):
        return False
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i >= x3 and i <= x4 and j >= y3 and j <= y4) or (i >= x5 and i <= x6 and j >= y5 and j <= y6):
                    if grid[i][j] != '.':
                        return False
                elif grid[i][j] != '#':
                    return False
        return True
    

def is_P(grid, x3, y3, x4, y4):
    x5, y5 = x3, y3
    x6, y6 = x3, y3
    while y6 + 1 < len(grid[0]) and grid[x6][y6] == '.':
        y6 += 1
    y6 -= 1
    while x6 + 1 < len(grid) and grid[x6][y6] == '.':
        x6 += 1
    x6 -= 1
    x3 = x4
    while x3 > 0 and grid[x3][y3] == '.':
        x3 -= 1
    x3 += 1
    if not (x1 < x5 <= x6 < x3 <= x2 and x2 == x4 and
            y1 < y5 and y5 == y3 and y3 <= y6 < y2 and y2 == y4):
        return False
    else:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i >= x3 and i <= x4 and j >= y3 and j <= y4) or (i >= x5 and i <= x6 and j >= y5 and j <= y6):
                    if grid[i][j] != '.':
                        return False
                elif grid[i][j] != '#':
                    return False
        return True
    

n = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))

x1, y1, x2, y2 = find_lighted(grid)

grid = border_lighted(grid, x1, y1, x2, y2)

x3, y3, x4, y4 = find_non_lighted(grid)

x1, y1, x2, y2 = find_lighted(grid)

if (x2 < 0 and y2 < 0): print('X')
elif is_I(grid): print('I')
elif is_O(grid, x3, y3, x4, y4): print('O')
elif is_C(grid, x3, y3, x4, y4): print('C')
elif is_L(grid, x3, y3, x4, y4): print('L')
elif is_H(grid, x3, y3, x4, y4): print('H')
elif is_P(grid, x3, y3, x4, y4): print('P')
else: print('X')

"""
5
#...#
#...#
#####
#...#
#...#

6
......
#####.
##..#.
##..#.
#####.
##....
"""