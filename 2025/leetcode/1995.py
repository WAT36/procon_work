class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans=0
        for i in range(3,len(nums)):
            for j in range(0,i):
                for k in range(j+1,i):
                    for l in range(k+1,i):
                        if nums[j]+nums[k]+nums[l]==nums[i]:
                            ans+=1
        return ans