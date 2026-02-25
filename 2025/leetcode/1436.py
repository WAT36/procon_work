class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        routemap={}
        for p in paths:
            routemap[p[0]]=p[1]
        ans=paths[0][0]
        while ans in routemap.keys():
            ans=routemap[ans]
        return ans
