class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        return max(len(list(filter(lambda x: x>0,nums))),len(list(filter(lambda x: x<0,nums))))