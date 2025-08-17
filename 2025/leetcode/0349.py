class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        ans=[]
        for i in range(len(nums2)):
            if nums2[i] in set1:
                ans.append(nums2[i])
        return list(set(ans))