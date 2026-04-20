class Solution:
    def totalMoney(self, n: int) -> int:
        ans=0
        for i in range(1,n+1):
            #print(i,((i-1)//7)+(i%7 if i%7!=0 else 7))
            ans+=((i-1)//7)+(i%7 if i%7!=0 else 7)
        return ans