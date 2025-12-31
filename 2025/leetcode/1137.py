class Solution:
    def tribonacci(self, n: int) -> int:
        ans=[0 for _ in range(0,n+1)]
        for i in range(0,n+1):
            if i==0:
                ans[i]=0
            elif i==1:
                ans[i]=1
            elif i==2:
                ans[i]=1
            else:
                ans[i]=ans[i-1]+ans[i-2]+ans[i-3]
        return ans[-1]
