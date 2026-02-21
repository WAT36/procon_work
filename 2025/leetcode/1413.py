class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minsum=999999999999
        sums=0
        for ni in nums:
            sums+=ni
            minsum=min(minsum,sums)
        if minsum > 0:
            return 1
        else:
            return abs(minsum)+1