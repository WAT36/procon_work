class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerocoords=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zerocoords.append([i,j])

        for k in range(len(zerocoords)):
            coord=zerocoords[k]
            for i in range(len(matrix)):
                matrix[i][coord[1]] = 0  
            for j in range(len(matrix[i])):
                matrix[coord[0]][j] = 0  
                       