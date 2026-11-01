class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        ansi=[]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        for n in nums:
            if n!=0:
                ansi.append(n)
        while len(ansi)<len(nums):
            ansi.append(0)
        return ansi