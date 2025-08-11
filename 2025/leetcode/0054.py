class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        checked = [[False for _ in range(m)] for _ in range(n)]
        lr=True
        ud=True
        wh=True
        ans=[]
        x,y=0,0
        #print(m,n)
        while len(ans) < m*n:
            #print(x,y,lr,ud,wh,ans)
            if not checked[y][x]:
                ans.append(matrix[y][x])
                checked[y][x]=True

            if wh:
                new_x=x+1 if lr else x-1
                if new_x<0 or m<=new_x or checked[y][new_x]:
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