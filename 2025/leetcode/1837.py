class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans=0
        i=0
        while n!=0:
            ans+=n%k
            n//=k
            print(ans,n,k)
        return ans
