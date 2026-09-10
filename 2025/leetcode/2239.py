class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans=9999999
        nums=sorted(nums)[::-1]
        for n in nums:
            if abs(n)<abs(ans):
                ans=n
        return ans
