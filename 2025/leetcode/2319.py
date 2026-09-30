class Solution:
    def checkXMatrix(self, grid: list[list[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i==j:
                    if grid[i][j]==0:
                        return False
                elif i+j==len(grid)-1:
                    if grid[i][j]==0:
                        return False
                else:
                    if grid[i][j]!=0:
                        return False
        return True
