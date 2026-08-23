class Solution:
    def countElements(self, nums: List[int]) -> int:
        return len(list(filter(lambda x:x > min(nums) and x < max(nums),nums)))