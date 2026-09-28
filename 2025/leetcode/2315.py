class Solution:
    def countAsterisks(self, s: str) -> int:
        ans=0
        flag=False
        for i in range(len(s)):
            if s[i]=='|':
                flag= not flag
            elif not flag and s[i]=='*':
                ans+=1
        return ans
