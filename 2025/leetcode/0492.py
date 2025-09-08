import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l=math.floor(math.sqrt(area))
        for li in range(l,area+1):
            if area%li == 0:
                return sorted([li,area//li])[::-1]
        return []