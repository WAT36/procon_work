class Solution:
    def checkString(self, s: str) -> bool:
        if 'b' not in s:
            return True
        i=s.index('b')
        while i<len(s):
            if s[i]=='a':
                return False
            i+=1
        return True