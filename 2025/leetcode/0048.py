import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        matrix_sub = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[j][n-i-1] = matrix_sub[i][j]
        