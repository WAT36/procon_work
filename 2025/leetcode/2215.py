class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        ans1 = [i for i in nums1 if i not in nums2]
        ans2 = [i for i in nums2 if i not in nums1]
        return [ans1,ans2]