class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=nums1
        l.extend(nums2)
        l.sort()
        if(len(l)%2==0):
            return (l[len(l)//2]+l[(len(l)//2)-1])/2
        else:
            return l[len(l)//2]