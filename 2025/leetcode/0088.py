class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = nums1[:m]
        ans += nums2[:n]
        ans.sort()
        for i in range(len(ans)):
            nums1[i] = ans[i]
        