class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]<0):
                    ans+=(len(grid[i])-j)
                    break
        return ans