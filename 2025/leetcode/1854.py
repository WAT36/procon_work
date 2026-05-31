class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        miny=min([x[0] for x in logs])
        maxy=max([x[1] for x in logs])
        ans=[999999,0]
        for x in range(miny,maxy+1):
            ansx=0
            for ys in logs:
                if ys[0]<=x and x<ys[1]:
                    ansx+=1
            if ansx>ans[1]:
                ans=[x,ansx]
            print(ans,x,ansx)
        return ans[0] 