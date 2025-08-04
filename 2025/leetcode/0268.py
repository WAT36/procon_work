class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        else:
            return len(nums)