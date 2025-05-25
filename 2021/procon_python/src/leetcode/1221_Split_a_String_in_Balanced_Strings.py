class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans=0
        balance=0
        for i in range(len(s)):
            if(s[i]=="L"):
                balance-=1
            else:
                balance+=1
            if(balance==0):
                ans+=1
        return ans