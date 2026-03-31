import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i  in range(max(nums)+1):
            ind=bisect.bisect_left(nums,i)
            if i == len(nums[ind:]):
                return i
        return -1