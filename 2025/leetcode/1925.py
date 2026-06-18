import math
class Solution:
    def countTriples(self, n: int) -> int:
        ans=[]
        for a in range(1,n+1):
            for b in range(1,n+1):
                cc=a*a + b*b
                c=int(math.sqrt(cc))
                if c*c == cc and c<=n:
                    print(a,b,c)
                    ans.append([a,b,c])
        return len(ans)

