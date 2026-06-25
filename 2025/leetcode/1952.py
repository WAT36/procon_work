class Solution:
    def isThree(self, n: int) -> bool:
        ans=0
        for i in range(1,n+1):
            if n%i==0:
                ans+=1
                if ans>3:
                    return False
        return ans==3