class Solution:
    def sortedSquares(self, A: list[int]) -> list[int]:
        ans=[]
        for i in range(len(A)):
            ans.append(A[i]**2)
        ans.sort()
        return ans