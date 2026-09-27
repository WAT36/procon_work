class Solution:
    def greatestLetter(self, s: str) -> str:
        ans=[""]
        for i in range(len(s)-1):
            if s[i].lower() in s and s[i].upper() in s:
                ans.append(s[i].upper())
        ans.sort()
        return ans[-1]