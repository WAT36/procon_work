class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans=9999999999
        for i in range(len(nums)):
            if i+k-1>=len(nums):
                break
            ans=min(ans,nums[i+k-1]-nums[i])
        return ans