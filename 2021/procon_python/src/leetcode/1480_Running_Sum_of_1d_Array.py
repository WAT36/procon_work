class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            ans.append(sum(nums[:i])+nums[i])
        return ans