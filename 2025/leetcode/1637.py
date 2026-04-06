class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[p[0] for p in points]
        x.sort()
        ans=0
        for i in range(len(x)-1):
            ans=max(ans,abs(x[i+1]-x[i]))
        return ans