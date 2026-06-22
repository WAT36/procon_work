class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s=list(s)
        count=s.count(s[0])
        for si in s:
            if count != s.count(si):
                return False
        return True