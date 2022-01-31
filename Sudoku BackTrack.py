#int SudokuGrid = [9,9]
SolutionGrid = [[0,0,2,5,0,0,0,3,0],
                [8,0,0,4,0,0,0,0,0],
                [5,0,6,3,0,8,0,7,0],
                [0,0,5,1,8,0,0,0,0],
                [0,2,7,6,0,9,1,4,0],
                [0,0,0,0,2,3,5,0,0],
                [0,7,0,8,0,5,9,0,1],
                [0,0,0,0,0,6,0,0,3],
                [0,3,0,0,0,7,4,0,0]]

def main():
    if(SolveGrid(SolutionGrid)):
        print("-" * 13)
        for x in range(0, len(SolutionGrid)):
            row = "|"
            for y in range(0, len(SolutionGrid)):
                row += str(SolutionGrid[x][y])
                if((y+1) % 3 == 0):
                    row += "|"
            print(row)
            if((x+1)%3 == 0):
                print("-" * 13)
    else:
        print("Impossible to solve")

def SolveGrid(SolutionGrid):

    NextEmpty = FindNextEmptyCell(SolutionGrid)
    if (NextEmpty == None):
        return True
    
    row = NextEmpty[0]
    column = NextEmpty[1]
    for x in range(1, 10):
        if(TileIsSafe(SolutionGrid, row, column, x)):
            
            SolutionGrid[row][column] = x

            if(SolveGrid(SolutionGrid)):
                return True

            SolutionGrid[row][column] = 0

    return False

    
#trying to figure out how backtracking works is a pain when you know that these below methods work 

def RowIsCorrect(InputGrid, currentX, currentY, num):
    #this is really annoying because it messes with my perception of x and y but here we are
    for y in range(0, len(InputGrid)):
        if(num == InputGrid[currentX][y] and currentY != y and InputGrid[currentX][y] != 0):
            return False
    return True

def ColumnIsCorrect(InputGrid, currentX, currentY, num):
    for x in range(0, len(InputGrid)):
        if(num == InputGrid[x][currentY] and currentX != x and InputGrid[x][currentY] != 0):
            return False
    return True

def GridIsCorrect(InputGrid, currentX, currentY, num):
    closestXMiddle = FindClosestMiddle(currentX)
    closestYMiddle = FindClosestMiddle(currentY)
    xOffset = -1
    yOffset = -1
    for x in range(0, len(InputGrid)):
        if(num == InputGrid[closestXMiddle + xOffset][closestYMiddle + yOffset]
        and closestXMiddle + xOffset != currentX and closestYMiddle + yOffset != currentY and InputGrid[closestXMiddle + xOffset][closestYMiddle + yOffset] != 0):
           return False
        elif yOffset == 1:
            yOffset = -1
            xOffset += 1
        else:
            yOffset += 1
    return True

def TileIsSafe(SolutionGrid, currentX, currentY, num):
    if (RowIsCorrect(SolutionGrid, currentX, currentY, num)
       and ColumnIsCorrect(SolutionGrid, currentX, currentY, num)
       and GridIsCorrect(SolutionGrid, currentX, currentY, num)):
        return True
    return False

def FindNextEmptyCell(InputGrid):
    for x in range(0, len(InputGrid)):
        for y in range(0, len(InputGrid)):
            if(InputGrid[x][y] == 0):
                return x,y
    return None

def FindClosestMiddle(inputCoord):
    middleOfGridNumbers = [1, 4, 7]
    return middleOfGridNumbers[min(range(len(middleOfGridNumbers)), key = lambda i: abs(middleOfGridNumbers[i]-inputCoord))]

main()

