class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        n =list(set(nums1) & set(nums2))
        return min(n) if len(n)>0 else -1