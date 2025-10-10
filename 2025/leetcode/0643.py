class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=-9999999999
        i=0
        ansi=sum(nums[i:i+k])
        while i+k-1<len(nums):
            ans=max(ans,ansi)
            ansi-=nums[i]
            ansi+=nums[i+k] if i+k <len(nums) else 0
            i+=1
        return ans/k
