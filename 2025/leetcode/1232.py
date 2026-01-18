class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates[1][0]==coordinates[0][0]:
            for c in coordinates:
                if c[0] != coordinates[0][0]:
                    return False
            return True            
        a=(coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        b=coordinates[0][1] - a*coordinates[0][0]
        for c in coordinates:
            if c[1] != a*c[0] + b:
                return False
        return True