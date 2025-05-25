class Solution:
    def commonChars(self, A: list[str]) -> list[str]:
        ans=list(A[0])
        for i in range(1,len(A)):
            ai=list(A[i])
            ansj=[]
            for j in range(len(ai)):
                try:
                    ind=ans.index(ai[j])
                    ansj.append(ans[ind])
                    ans.pop(ind)
                except ValueError:
                    pass
            ans=ansj
        return ans