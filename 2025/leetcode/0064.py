class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dpgrid=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i>0 and j>0:
                    dpgrid[i][j] = min(dpgrid[i-1][j]+grid[i][j],dpgrid[i][j-1]+grid[i][j])
                elif i>0:
                    dpgrid[i][j] = dpgrid[i-1][j] + grid[i][j]
                elif j>0:
                    dpgrid[i][j] = dpgrid[i][j-1] + grid[i][j]
                else:
                    dpgrid[i][j] = grid[i][j]
        return dpgrid[m-1][n-1]