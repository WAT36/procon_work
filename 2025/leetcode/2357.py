class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ans=0
        while True:
            ni=list(filter(lambda x: x>0,nums))
            if len(ni)==0:
                break
            ni.sort()
            x=ni[0]
            nums=[nums[i]-x for i in range(len(nums))]
            ans+=1
        return ans