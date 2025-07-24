class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNum=set(nums)
        if len(nums) == len(setNum):
            return False
        else:
            return True