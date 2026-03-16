class Solution:
    def makeGood(self, s: str) -> str:
        ans=""
        while True:
            i=0
            ansi=""
            while i<len(s)-1:
                if s[i]!=s[i+1] and s[i].lower() == s[i+1].lower():
                    i+=1
                else:
                    ansi=ansi+s[i]
                i+=1
            if i==len(s)-1:
                ansi=ansi+s[i]
            if ans == ansi:
                break
            ans=ansi
            s=ansi
        return ans
        