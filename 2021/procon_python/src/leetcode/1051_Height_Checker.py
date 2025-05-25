class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        right_order=sorted(heights)
        ans=0
        for i in range(len(heights)):
            if(heights[i] != right_order[i]):
                ans+=1
        return ans