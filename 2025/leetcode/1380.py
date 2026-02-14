class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        lerow=[]
        lecolumn=[]
        for i in range(len(matrix)):
            minri=min(matrix[i])
            j=matrix[i].index(minri)
            lerow.append([i,j])
        
        yoko=len(matrix[0])
        for j in range(yoko):
            cj=[matrix[i][j] for i in  range(len(matrix))]
            maxcj=max(cj)
            i=cj.index(maxcj)
            lecolumn.append([i,j])
        
        anse=[]
        for eri in lerow:
            if eri in lecolumn:
                anse.append(eri)

        print(lerow)
        print(lecolumn)
        print(anse)

        if len(anse)==0:
            return []
        
        ans=[]
        for ansi in anse:
            print(ansi)
            i=ansi[0]
            j=ansi[1]
            print(i,j)
            ans.append(matrix[i][j])
        return ans


