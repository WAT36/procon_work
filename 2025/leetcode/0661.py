class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ans=[[0 for _ in range(len(img[0]) if len(img)>0 else 0)] for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[i])):
                cellSum=0
                cellCount=0
                if i>0 and j>0:
                    cellSum+=img[i-1][j-1]
                    cellCount+=1
                if i>0:
                    cellSum+=img[i-1][j]
                    cellCount+=1
                if i>0 and j<len(img[i])-1:
                    cellSum+=img[i-1][j+1]
                    cellCount+=1

                if j>0:
                    cellSum+=img[i][j-1]
                    cellCount+=1
                cellSum+=img[i][j]
                cellCount+=1
                if j<len(img[i])-1:
                    cellSum+=img[i][j+1]
                    cellCount+=1

                if i<len(img)-1 and j>0:
                    cellSum+=img[i+1][j-1]
                    cellCount+=1
                if i<len(img)-1:
                    cellSum+=img[i+1][j]
                    cellCount+=1
                if i<len(img)-1 and j<len(img[i])-1:
                    cellSum+=img[i+1][j+1]
                    cellCount+=1
                ans[i][j]=cellSum//cellCount
        return ans