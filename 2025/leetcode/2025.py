class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original):
            return  []
        ans=[]
        for _ in range(m):
            ans.append(original[:n])
            original=original[n:]
        return ans