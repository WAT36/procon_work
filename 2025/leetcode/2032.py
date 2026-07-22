class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s=set([])
        for i in range(len(nums1)):
            if nums1[i] in nums2 or nums1[i] in nums3:
                s.add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] in nums1 or nums2[i] in nums3:
                s.add(nums2[i])
        for i in range(len(nums3)):
            if nums3[i] in nums1 or nums3[i] in nums2:
                s.add(nums3[i])
        return list(s)
