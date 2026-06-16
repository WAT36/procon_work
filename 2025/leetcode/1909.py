class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count=0
        for i in range(len(nums)):
            if (i>0 and nums[i-1]>=nums[i]):
                if (i>1 and nums[i-2]>=nums[i]) and (i<len(nums)-1 and nums[i-1] >= nums[i+1]):
                    return False
                else:
                    count+=1
        return count<=1