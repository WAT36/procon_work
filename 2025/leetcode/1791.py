class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ecount=[]
        for e in edges:
            if len(ecount) <= max(e):
                while len(ecount) <= max(e):
                    ecount.append(0)
            ecount[e[0]]+=1
            ecount[e[1]]+=1
        return ecount.index(max(ecount))
