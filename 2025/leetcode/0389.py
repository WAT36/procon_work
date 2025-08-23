class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = ''.join(sorted(list(s)))
        t = ''.join(sorted(list(t)))
        for i in range(len(s)):
            if s[i] !=  t[i]:
                return t[i]
        else:
            return t[-1]