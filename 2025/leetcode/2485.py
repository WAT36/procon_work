import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        i=int(math.sqrt((n/2)*(n+1)))
        if i*i==n*(n+1)//2:
            return i
        else:
            return -1