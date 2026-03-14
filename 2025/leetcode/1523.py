class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans=0
        while low % 2 != 0:
            ans+=1
            low+=1
        while high % 2 != 0:
            ans+=1
            high-=1
        ans+=(high-low)//2
        return ans