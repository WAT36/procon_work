import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first=[matrix[i][0] for i in range(len(matrix))]
        ind = bisect.bisect_right(first,target) - 1
        #print(ind)
        return target in matrix[ind]