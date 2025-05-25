class Solution:
    def peakIndexInMountainArray(self, A: list[int]) -> int:
        max_a=max(A)
        return A.index(max_a)
