class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans=0
        for a1i in arr1:
            for a2j in arr2:
                if abs(a1i-a2j) <= d:
                    break
            else:
                ans+=1
        return ans