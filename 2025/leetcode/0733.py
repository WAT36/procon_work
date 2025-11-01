class Solution:
    def recurFloodFill(self, image: List[List[int]], sr: int, sc: int, color: int, originval: int) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        image[sr][sc]=color
        #print(sr,sc,color,originval)

        if 0<sr and image[sr-1][sc] == originval and image[sr-1][sc] != color:
            image=self.recurFloodFill(image,sr-1,sc,color, originval)
        if sr<m-1 and image[sr+1][sc] == originval and image[sr+1][sc] != color:
            image=self.recurFloodFill(image,sr+1,sc,color, originval)
        if 0<sc and image[sr][sc-1] == originval and image[sr][sc-1] != color:
            image=self.recurFloodFill(image,sr,sc-1,color, originval)
        if sc<n-1 and image[sr][sc+1] == originval and image[sr][sc+1] != color:
            image=self.recurFloodFill(image,sr,sc+1,color, originval)
        return image

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return self.recurFloodFill(image,sr,sc,color,image[sr][sc])

        
