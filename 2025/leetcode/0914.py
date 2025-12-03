import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        m={}
        for d in deck:
            if d not in m.keys():
                m[d]=1
            else:
                md=m[d]
                m[d]=md+1
        v = list(m.values())
        gcd=math.gcd(*v)
        if gcd == 1:
            return False
        else:
            return True        