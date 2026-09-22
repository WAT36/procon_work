class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums)>1:
            newnums=[]
            i=0
            while i<len(nums):
                newnums.append(min(nums[i],nums[i+1]))
                if i+3<=len(nums):
                    newnums.append(max(nums[i+2],nums[i+3]))
                i+=4
            nums=newnums
        return nums[-1]