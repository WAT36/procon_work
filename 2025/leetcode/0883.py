class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans=0
        xy=0
        xz=0
        yz=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]>0:
                    xy+=1
                if j==len(yz):
                    yz.append(grid[i][j])
                else:
                    yz[j]=max(yz[j],grid[i][j])
            xz+=max(grid[i])
        return xy+xz+sum(yz)