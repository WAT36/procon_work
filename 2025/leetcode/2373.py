class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n=len(grid)
        ans=[[-1 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                ansij=[*grid[i][j:j+3],*grid[i+1][j:j+3],*grid[i+2][j:j+3]]
                ans[i][j]=max(ansij)
        return ans
