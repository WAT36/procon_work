class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        ans=[]
        for i in range(len(nums)):
            ans.insert(index[i],nums[i])
        return ans