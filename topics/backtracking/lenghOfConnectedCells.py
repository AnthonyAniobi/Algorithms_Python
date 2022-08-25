def lengthOfConnectedCells(matrix)->int:
    rowLength:int = len(matrix)
    colLength:int = len(matrix[0])
    emptyMatrix = [[0 for x in range(rowLength)] for y in range(colLength)]
    max_connected = 0

    def movingCounter(i, j):
        if i<0 or i==rowLength or j<0 or j==colLength:
            return 0
        if emptyMatrix[i][j]==1:
            return 0
        elif matrix[i][j] == 0:
            emptyMatrix[i][j] = 1
            return 0
        else:
            emptyMatrix[i][j] = 1 # update the empty matrix
            top:int = 1+movingCounter( i, j-1)
            bottom:int = 1+movingCounter(i, j+1)
            topRight:int = 1+movingCounter( i+1, j-1)
            topLeft:int = 1+movingCounter( i-1, j-1)
            bottomRight:int = 1+movingCounter( i+1, j+1)
            bottomLeft:int = 1+movingCounter( i-1, j+1)
            left:int = 1+movingCounter( i-1, j)
            right:int = 1+movingCounter( i+1, j)
            return max([top, bottom, left, right, topRight, topLeft, bottomLeft, bottomRight])

    for i in range(rowLength):
        for j in range(colLength):
            max_connected = max( [max_connected, movingCounter( i, j)])
    return max_connected



if __name__ == '__main__':
    matrix:list = [
        [1,1,0,0,0],
        [0,1,1,0,0],
        [0,1,1,0,1],
        [1,0,0,0,1],
        [0,1,0,1,1],
    ]
    result = lengthOfConnectedCells(matrix)
    print(f'length of connected cells = {result}')