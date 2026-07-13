class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i==0 and sum(nums[i+1:])==0:
                return 0
            elif i==len(nums)-1:
                if sum(nums[:len(nums)-1]) == 0:
                    return i
                else:
                    return -1
            elif sum(nums[:i]) == sum(nums[i+1:]):
                return i