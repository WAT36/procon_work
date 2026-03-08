class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points=[[0,0]]
        now=[0,0]
        for i in range(len(path)):
            if path[i]=='N':
                now=[now[0],now[1]+1]
            elif path[i]=='E':
                now=[now[0]+1,now[1]]
            elif path[i]=='W':
                now=[now[0]-1,now[1]]
            elif path[i]=='S':
                now=[now[0],now[1]-1]
            if now in points:
                return True
            points.append(now)
        return False
