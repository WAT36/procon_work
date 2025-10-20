class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans=0
        cont=0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                cont+=1
            else:
                ans=max(ans,cont+1)
                cont=0
        else:
            ans=max(ans,cont+1)
        return ans