class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=""
        ansi=""
        for i in range(len(s)):
            if i>0:
                if s[i-1]!=s[i]:
                    if len(ansi)<3:
                        ans=ans+ansi
                        ansi=s[i]
                    else:
                        ans=ans+ansi[:2]
                        ansi=s[i]
                else:
                    ansi=ansi+s[i]
            else:
                ansi=ansi+s[i]
        else:
            if len(ansi)<3:
                ans=ans+ansi
                ansi=s[i]
            else:
                ans=ans+ansi[:2]
                ansi=s[i]
        return ans