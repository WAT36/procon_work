class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        a=("01"*n)[:n]
        b=("10"*n)[:n]
        ansa=0
        ansb=0
        for i in range(n):
            if s[i]!=a[i]:
                ansa+=1
            if s[i]!=b[i]:
                ansb+=1
        return min(ansa,ansb)