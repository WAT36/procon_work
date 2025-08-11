class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxcanjump = 0
        for i in range(len(nums)):
            if maxcanjump < i:
                return False
            if maxcanjump < i + nums[i]:
                maxcanjump = i + nums[i]
        return True
        