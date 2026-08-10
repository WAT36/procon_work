class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        ansi=sorted(nums)[-1*k:]
        ans=[]
        for i in range(len(nums)):
            if nums[i] in ansi:
                ans.append(nums[i])
                ansi.remove(nums[i])
        return ans