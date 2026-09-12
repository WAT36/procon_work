class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        ans=nums[0]
        for ni in nums:
            ans=list(set(ans) & set(ni))
        ans.sort()
        return ans