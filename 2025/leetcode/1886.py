class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if  mat == target:
            return True
        
        mat1=[[-1 for _  in range(len(mat[0]))] for _ in range(len(mat))]
        for i in  range(len(mat)):
            for j in range(len(mat[i])):
                mat1[i][j]=mat[len(mat[i])-1-j][i]
        print(mat1)
        if  mat1 == target:
            return True

        mat1=[[-1 for _  in range(len(mat[0]))] for _ in range(len(mat))]
        for i in  range(len(mat)):
            for j in range(len(mat[i])):
                mat1[i][j]=mat[len(mat)-1-i][len(mat[i])-1-j]
        print(mat1)
        if  mat1 == target:
            return True

        mat1=[[-1 for _  in range(len(mat[0]))] for _ in range(len(mat))]
        for i in  range(len(mat)):
            for j in range(len(mat[i])):
                mat1[i][j]=mat[j][len(mat)-1-i]
        print(mat1)
        if  mat1 == target:
            return True
        
        return False