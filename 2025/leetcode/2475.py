class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    continue
                for k in range(j+1,len(nums)):
                    if nums[j]==nums[k] or nums[i]==nums[k]:
                        continue
                    ans.append([i,j,k])
        return len(ans)