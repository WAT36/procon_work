# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=1
        right=n
        while left<right:
            med=(left+right)//2
            if left == med or right == med:
                break
            elif isBadVersion(med):
                right=med
            else:
                left=med
        for i in range(left,right+1):
            if isBadVersion(i):
                return i
