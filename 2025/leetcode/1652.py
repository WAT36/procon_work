class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(code)):
            ansi=0
            if k>0:
                for j in range(1,k+1):
                    ansi+=code[(i+j)%len(code)]
            elif k<0:
                for j in range(-1,k-1,-1):
                    ansi+=code[(i+j)%len(code)]
            ans.append(ansi)
        return ans