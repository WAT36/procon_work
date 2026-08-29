class Solution:
    def countEven(self, num: int) -> int:
        ans=0
        for i in range(1,num+1):
            ansi=0
            stri=str(i)
            for j in range(len(stri)):
                ansi+=int(stri[j])
            if ansi%2==0:
                ans+=1
        return ans