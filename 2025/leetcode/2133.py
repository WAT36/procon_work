class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            if len(matrix[i]) != len(list(set(matrix[i]))):
                return False
            
            j=[matrix[ii][i] for ii in range(len(matrix))]
            if len(j) != len(list(set(j))):
                return False
        return True
