class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        i=0
        while True:
            if start-i>=0 and nums[start-i]==target:
                return i
            if start+i<len(nums) and nums[start+i]==target:
                return i            
            i+=1