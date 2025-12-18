class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[1] == points[2] or points[2] == points[0]:
            return False
        if points[0][0] == points[1][0]:
            return points[2][0] != points[0][0]
        if points[0][0] == points[2][0]:
            return points[1][0] != points[0][0]
        a1=(points[1][1]-points[0][1])/(points[1][0]-points[0][0])
        a2=(points[2][1]-points[0][1])/(points[2][0]-points[0][0])
        return a1 != a2
