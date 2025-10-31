class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        rightsum=sum(nums)
        for i in range(len(nums)):
            leftsum+=nums[i-1] if i-1>=0 else 0
            rightsum-=nums[i] if i<len(nums) else 0
            print(i,leftsum,rightsum)
            if leftsum == rightsum:
                return i
        return -1