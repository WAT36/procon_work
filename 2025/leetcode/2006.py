class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)-1):
            ans+=nums[i+1:].count(nums[i]-k)s
            ans+=nums[i+1:].count(nums[i]+k)
        return ans