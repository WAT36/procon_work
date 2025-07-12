import bisect
class Solution:
    def isNearTarget(self,target:int,ans:int,val:int):
        return abs(target-val) < abs(target-ans)

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=100000000
        nums=sorted(nums)
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                numsk = target - (nums[i]+nums[j])
                if(numsk > nums[-1] and self.isNearTarget(target,ans,nums[i]+nums[j]+nums[-1])):
                    ans = nums[i]+nums[j]+nums[-1]
                    continue
                
                nums_rest=nums[j+1:]
                ind = bisect.bisect_left(nums_rest,numsk)
                if(ind == len(nums_rest)):
                    ind-=1
                #print(i,j,nums_rest,ind,numsk,ans)
                if(self.isNearTarget(target,ans,nums[i]+nums[j]+nums_rest[ind])):
                    ans = nums[i]+nums[j]+nums_rest[ind]
                
                if(ind+1<len(nums_rest) and self.isNearTarget(target,ans,nums[i]+nums[j]+nums_rest[ind+1])):
                    ans = nums[i]+nums[j]+nums_rest[ind+1]

                if(ind-1>=0 and self.isNearTarget(target,ans,nums[i]+nums[j]+nums_rest[ind-1])):
                    ans = nums[i]+nums[j]+nums_rest[ind-1]
        return ans




        