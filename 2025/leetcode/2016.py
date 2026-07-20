class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans=-1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):s
                if nums[i]<nums[j] and ans<nums[j]-nums[i]:
                    ans=nums[j]-nums[i]
        return ans