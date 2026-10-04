class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        nums.sort()
        count=0
        ans=[]
        i=0
        while i<len(nums):
            if i+1>=len(nums):
                ans.append(nums[i])
                i+=1
            elif nums[i]==nums[i+1]:
                count+=1
                i+=2
            else:
                ans.append(nums[i])
                i+=1
        return [count,len(ans)]
