class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        dm={}
        for i in range(rows):
            for j in range(cols):
                dist=abs(rCenter-i)+abs(cCenter-j)
                if dist in dm.keys():
                    darr=dm[dist]
                    darr.append([i,j])
                    dm[dist]=darr
                else:
                    dm[dist]=[[i,j]]
        ans=[]
        key=list(dm.keys())
        key.sort()
        for k in key:
            dmk=dm[k]
            #print(k,dmk)
            ans=ans+dmk
        return ans