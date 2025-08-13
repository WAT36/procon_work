import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        x = int(round(math.log(n,4)))
        return 4 ** x  == n