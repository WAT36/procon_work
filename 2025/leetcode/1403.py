class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nums=sorted(nums)[::-1]
        for i in range(len(nums)+1):
            ansi=nums[:i]
            notansi=nums[i:]
            if sum(ansi) > sum(notansi):
                return ansi
