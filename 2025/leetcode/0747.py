class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_c=sorted(nums)
        if nums_c[-2]*2 > nums_c[-1]:
            return -1
        else:
            return nums.index(nums_c[-1])
