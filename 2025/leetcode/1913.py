class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums=sorted(nums)
        mins=nums[0]*nums[1]
        maxs=nums[-1]*nums[-2]
        return maxs-mins