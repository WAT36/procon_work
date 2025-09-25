class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c:
            return mat
        ans=[]
        matarr=[]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                matarr.append(mat[i][j])
        k=0
        for i in range(r):
            ansi=[]
            for j in range(c):
                ansi.append(matarr[k])
                k+=1
            ans.append(ansi)
        return ans