class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        ans=0
        c=sorted(cost)[::-1]
        i=0
        while i<len(c):
            ans+=c[i]
            i+=1
            if i>=len(c):
                break
            ans+=c[i]
            i+=2
        return ans