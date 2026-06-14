class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        rowFlag = [0] * rows
        colFlag = [0] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rowFlag[row] = 1
                    colFlag[col] = 1
        
        for i in range(len(rowFlag)):
            for j in range(len(colFlag)):
                if rowFlag[i] == 1 or colFlag[j] == 1:
                    matrix[i][j] = 0
    
        
        