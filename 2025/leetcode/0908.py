class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        nums.sort()
        minplusk=min(nums)+k
        maxminusk=max(nums)-k
        if maxminusk <= minplusk:
            return 0
        return abs(maxminusk-minplusk)