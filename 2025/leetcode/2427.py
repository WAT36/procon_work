import math
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans=0
        n=math.gcd(a,b)
        for i in range(1,n+1):
            if n%i==0:
                ans+=1
        return ans