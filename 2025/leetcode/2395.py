class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        sumarr=[]
        for i in range(len(nums)-1):
            sumi=nums[i]+nums[i+1]
            if sumi in sumarr:
                return True
            else:
                sumarr.append(sumi)
        return False