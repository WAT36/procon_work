class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums is None or len(nums) == 0:
            return []
        ans=[]
        start=None
        diff=0
        for i in range(len(nums)):
            if start is None:
                start=nums[i]
                diff=1
            elif(start+diff==nums[i]):
                diff+=1
            else:
                ans.append(str(start)+"->"+str(nums[i-1]) if diff>1 else str(start))
                start=nums[i]
                diff=1
        else:
            ans.append(str(start)+"->"+str(nums[i]) if diff>1 else str(start))
        return ans
