class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        ans=0
        for i in range(len(nums)):
            if i+2<len(nums) and ans>nums[i]+nums[i+1]+nums[i+2]:
                break
            for j in range(i+1,len(nums)):
                if j+1<len(nums) and ans>nums[i]+nums[j]+nums[j+1]:
                    break
                for k in range(j+1,len(nums)):
                    if (nums[i]<nums[j]+nums[k] and nums[j]<nums[k]+nums[i] and nums[k]<nums[i]+nums[j]):
                        if ans<nums[i]+nums[j]+nums[k]:
                            ans=nums[i]+nums[j]+nums[k]
                        else:
                            break
                    else:
                        break
        return ans