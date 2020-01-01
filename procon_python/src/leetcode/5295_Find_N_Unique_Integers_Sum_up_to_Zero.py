class Solution:
    def sumZero(self, n: int) -> list[int]:
        ans=[]
        if(n%2!=0):
            ans.append(0)
            n-=1

        for i in range(1,n+1,2):
            ans.append(i)
            ans.append(-1*i)

        return ans

