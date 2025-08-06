class Solution:
    def jump(self, nums: List[int]) -> int:
        dparr=[0] * len(nums)
        for i in range(len(nums)-2,-1,-1):
            canmove=nums[i]
            dparr[i] = 10**10 if canmove == 0 else min(dparr[i+1:min(i+canmove+1,len(dparr))])+1
            #print(i,dparr)
        return dparr[0]