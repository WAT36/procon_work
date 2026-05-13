class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        onei=s.index('1')
        for i in  range(len(s)):
            if s[i]=='1':
                if abs(onei-i)<=1:
                    onei=i
                else:
                    return False
        return True