class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans=0
        while len(nums)>0:
            if len(nums)==1:
                ans+=nums[0]
                nums.pop()
            else:
                a=nums.pop(0)
                b=nums.pop(-1)
                ans+=int(str(a)+str(b))
        return ans