class Solution:
    def maxPower(self, s: str) -> int:
        ans=1
        ansi=1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                ansi+=1
            else:
                if ans < ansi:
                    ans=ansi
                ansi=1
        else:
            if ans < ansi:
                ans=ansi
            ansi=1
        return ans