class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dm={}
        for d in dominoes:
            ds=sorted(d)
            di=str(ds[0])+str(ds[1])
            if di in list(dm.keys()):
                dki=dm[di]
                dki+=1
                dm[di]=dki
            else:
                dm[di]=1
        ans=0
        for v in dm.values():
            if v==1:
                continue
            else:
                ans+=v*(v-1)//2
        return ans
        