class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [[nums[0]]]
        ans=[]
        for i in range(len(nums)):
            restnums=nums[:i]+nums[i+1:]
            arrs= self.permute(nums=restnums)
            for j in range(len(arrs)):
                arrs[j].insert(0,nums[i])
            ans.extend(arrs)
        #print(nums,ans)
        return ans
        