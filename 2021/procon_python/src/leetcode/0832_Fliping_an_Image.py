class Solution:
    def flipAndInvertImage(self, A: list[list[int]]) -> list[list[int]]:
        ans=[]
        for i in range(len(A)):
            ai=A[i]
            ai.reverse()
            ans_ai=[]
            for j in range(len(ai)):
                ans_ai.append((ai[j]+1)%2)
            ans.append(ans_ai)
        return ans