class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort()
        nums=nums[::-1]
        for n in nums:
            if n<0:
                return -1
            if -1*n in nums:
                return n
        return -1