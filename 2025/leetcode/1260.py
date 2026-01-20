class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        val=[]
        for g in grid:
            val=val+g
        k=k%(m*n)
        val=val[-k:]+val[:-k]
        ans=[]
        for i in range(m):
            ans.append(val[:n])
            val=val[n:]
        return ans