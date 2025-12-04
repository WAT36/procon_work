class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans=list(s)
        ri=-1
        i=0
        while i<len(s) and ri>=-1*len(s):
            if  ("a"<=s[ri] and s[ri]<="z") or ("A"<=s[ri] and s[ri]<="Z"):
                if  ("a"<=s[i] and s[i]<="z") or ("A"<=s[i] and s[i]<="Z"):
                    ans[i]=s[ri]
                    ri-=1
                    i+=1
                else:
                    i+=1
            else:
                ri-=1
        return ''.join(ans)