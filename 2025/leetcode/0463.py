class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans_out=0
        ans_in=0
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    if i==0:
                        ans_out+=1
                    if (i>0 and grid[i-1][j] == 0):
                        ans_in+=1
                    if i==row-1:
                        ans_out+=1
                    if (i<row-1 and grid[i+1][j] == 0):
                        ans_in+=1
                    if j==0:
                        ans_out+=1
                    if (j>0 and grid[i][j-1] == 0):
                        ans_in+=1
                    if j==col-1:
                        ans_out+=1                    
                    if (j<col-1 and grid[i][j+1] == 0):
                        ans_in+=1
                    #print(i,j,ans_out,ans_in)
        #print(ans_out,ans_in)
        return ans_out + ans_in
