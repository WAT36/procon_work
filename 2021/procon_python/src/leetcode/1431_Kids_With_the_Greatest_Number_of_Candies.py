class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy=max(candies)
        ans=[]
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=max_candy):
                ans.append(True)
            else:
                ans.append(False)
        return ans