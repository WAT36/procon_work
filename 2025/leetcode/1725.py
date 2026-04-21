class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sq=[]
        for r in rectangles:
            sq.append(min(r))
        maxsq=max(sq)
        return sq.count(maxsq)