DIRS = [[0,1],[1,0],[0,-1],[-1,0]]

def main():
    grid = formGrid(
"/Users/oliverwolff/Desktop/CS 3:4/advent-of-code-template/problems/prob8/testInput.txt")
    print(getTotalVisible(grid))   

def getTotalVisible(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    total = 0

    for i in range(0, nrows): 
        for j in range(0, ncols):
            if isVisible(grid, i, j): total += 1
    return total

def isVisible(grid, row, col):
    for dir in DIRS:
        if(isVisibleDir(grid, row, col, dir)) : return True
    return False

def isVisibleDir(grid, row, col, dir):
    value = grid[row][col]
    testRow = row + dir[0]
    testCol = col + dir[1]
    nrows = len(grid)
    ncols = len(grid[0])
    if(isOnEdge(grid, row, col)): return True
    while(isInBounds(grid, testRow, testCol)) :
        if( grid[testRow][testCol] < value 
        and isOnEdge(grid, testRow, testCol)):
            return True
        testRow += dir[0]
        testCol += dir[1]
    return False

def isOnEdge(grid, row, col):
    nrows = len(grid)
    ncols = len(grid[0])
    if(not isInBounds(grid, row, col)): return False
    if(row == nrows-1 or row == 0 or col == nrows-1 or col == 0): 
        return True
    return False

def isInBounds(grid, row, col):
    nrows = len(grid)
    ncols = len(grid[0])
    if(row >= nrows or row < 0 or col >= nrows or col < 0): 
        return False
    return True


## forms a 2d list of the given file
def formGrid(filePath):
    grid = []
    str = []
    with open (filePath) as file:
        for line in file: 
            for char in line: 
                if char == '\n' : break
                str.append(int(char))
            grid.append(str)
            str = []
    return grid

main()