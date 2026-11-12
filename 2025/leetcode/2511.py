class Solution:
    def captureForts(self, forts: list[int]) -> int:
        ans=0
        for i in range(len(forts)):
            if forts[i]!=1:
                continue
            for j in range(len(forts)):
                if forts[j]==-1:
                    fij=forts[min(i,j)+1:max(i,j)]
                    if 1 not in fij and -1 not in fij:
                        ans=max(ans,fij.count(0))
                        #print(i,j,ans)
        return ans