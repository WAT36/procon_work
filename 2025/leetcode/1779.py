class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ansp=[]
        for p  in  points:
            if p[0]==x:
                ansp.append(p)
            if p[1]==y:
                ansp.append(p)
        ans=99999999999
        finalans=[]
        for a in ansp:
            if abs(a[0]-x)+abs(a[1]-y) < ans:
                ans=abs(a[0]-x)+abs(a[1]-y)
                finalans=a
        return points.index(finalans) if finalans!=[] else -1