class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        checked = [[False for _ in range(n)] for _ in range(n)]
        lr=True
        ud=True
        wh=True
        ans = [[False for _ in range(n)] for _ in range(n)]
        x,y=0,0
        i=1
        #print(m,n)
        while i <= n*n:
            #print(x,y,lr,ud,wh,ans)
            if not checked[y][x]:
                ans[y][x]=i
                checked[y][x]=True
                i+=1
            if wh:
                new_x=x+1 if lr else x-1
                if new_x<0 or n<=new_x or checked[y][new_x]:
                    wh = not wh
                    lr = not lr
                else:
                    x=new_x
            else:
                new_y=y+1 if ud else y-1
                if new_y<0 or n<=new_y or checked[new_y][x]:
                    wh = not wh
                    ud = not ud
                else:
                    y=new_y
        return ans     