class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans=[]
        for i in range(len(s)):
            if s[i] in ans:
                return s[i]
            else:
                ans.append(s[i])