class Solution:
    def distinctIntegers(self, n: int) -> int:
        x=[n]
        while True:
            lenx=len(x)
            xn=[]
            for xi in x:
                for j in range(1,xi):
                    if xi%j==1:
                        xn.append(j)
            x=list(set(x+xn))
            if lenx==len(x):
                break
        return len(x)