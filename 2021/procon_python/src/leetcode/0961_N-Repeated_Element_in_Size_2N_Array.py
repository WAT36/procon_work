class Solution:
    def repeatedNTimes(self, A: list[int]) -> int:
        n=len(A)//2
        ans=0
        for i in range(len(A)):
            if(n==A.count(A[i])):
                ans=A[i]
                break
        return ans