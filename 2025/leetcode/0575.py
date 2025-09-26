class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ans=len(candyType)//2
        return min(ans,len(set(candyType)))