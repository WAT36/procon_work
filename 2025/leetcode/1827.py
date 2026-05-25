class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            if i==0:
                continue
            if nums[i]>nums[i-1]:
                continue
            else:
                ans+=(nums[i-1]-nums[i])+1
                nums[i]=nums[i-1]+1
        return ans