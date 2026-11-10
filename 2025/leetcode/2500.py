class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        ans=0
        while True:
            gi=[]
            maxgi=[]
            for g in grid:
                if len(g)==0:
                    continue
                maxg=max(g)
                #while maxg in g:
                g.remove(maxg)
                gi.append(g)
                maxgi.append(maxg)
            if len(maxgi)==0:
                break
            ans+=max(maxgi)
            grid=gi
            #print(ans,maxgi,grid)
        return ans
