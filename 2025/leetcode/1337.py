class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans=[[] for _ in range(len(mat[0])+1)]
        for i in range(len(mat)):
            #print(i,mat[i],mat[i].count(1),ans)
            ans[mat[i].count(1)].append(i)
        ans2=[]
        i=0
        while len(ans2)<k:
            ans2=ans2+ans[i]
            i+=1
        return ans2[:k]