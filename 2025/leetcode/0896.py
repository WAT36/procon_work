class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] == max(nums):
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False
            return True
        elif nums[-1] == max(nums):
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
            return True        
        else:
            return False