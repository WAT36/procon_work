import bisect
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums=sorted(nums)
        ans=[]
        for i in range(len(nums)):
            ans.append(bisect.bisect_left(sorted_nums,nums[i]))
        return ans