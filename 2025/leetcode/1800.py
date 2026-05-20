class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans=0
        maxi=0
        for i in range(len(nums)):
            maxi+=nums[i]
            if i<len(nums)-1 and nums[i] >= nums[i+1]:
                ans=max(ans,maxi)
                maxi=0
            #print(i,nums[i],maxi,ans)
        else:
            ans=max(ans,maxi)
        return ans