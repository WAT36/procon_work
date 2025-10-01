class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []:
            return m*n
        min_a=9999999999
        min_b=9999999999
        for oi in ops:
            min_a=min(min_a,oi[0])
            min_b=min(min_b,oi[1])
        return min_a*min_b