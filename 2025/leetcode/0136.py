class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        i=0
        while i<len(nums):
            if(i==len(nums)-1 or nums[i]!=nums[i+1]):
                return nums[i]
            i+=2