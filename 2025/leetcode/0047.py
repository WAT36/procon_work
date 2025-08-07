class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return []
        elif len(nums)==1:
            return [[nums[0]]]
        ans=[]
        for i in range(len(nums)):
            restnums=nums[:i]+nums[i+1:]
            arrs= self.permuteUnique(nums=restnums)
            for j in range(len(arrs)):
                arrs[j].insert(0,nums[i])
            ans.extend(arrs)
        #print(nums,ans)
        ans2=[]
        for i in range(len(ans)):
            if ans[i] not in ans2:
                ans2.append(ans[i])
        return ans2
        