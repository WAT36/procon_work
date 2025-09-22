class Solution:
    def checkRecord(self, s: str) -> bool:
        a=0
        l=0
        for i in range(len(s)):
            if s[i] == 'A':
                a+=1
                l=0
            elif s[i] == 'L':
                l+=1
                if i>0 and s[i-1]=='L' and l>=3:
                    return False
            else:
                l=0
        else:
            if a>=2 or l>=3:
                return False
        return True

