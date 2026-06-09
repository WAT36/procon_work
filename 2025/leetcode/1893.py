class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left,right+1):
            for r in ranges:
                if r[0]<=i and i<=r[1]:
                    break
            else:
                return False
        return True