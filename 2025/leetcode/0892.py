class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans=0
        for gi in grid:
            for gij in gi:
                ans+=(gij*4)+2 if gij > 0 else 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if j<len(grid[i])-1:
                    ans-=min(grid[i][j],grid[i][j+1])*2
                if i<len(grid)-1:
                    ans-=min(grid[i][j],grid[i+1][j])*2
        return ans
