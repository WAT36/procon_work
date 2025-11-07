class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        arr=matrix[0]
        for i in range(1,len(matrix)):
            arri=matrix[i]
            if arr[:-1] != arri[1:]:
                return False
            arr=arri
        return True