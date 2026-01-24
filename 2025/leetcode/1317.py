class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            a=i
            b=n-i
            if '0' not in str(a) and '0' not in str(b):
                return [a,b] 