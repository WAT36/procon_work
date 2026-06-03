class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count=[0,0]
        now=0
        for i in range(len(s)):
            now+=1
            if i<len(s)-1:
                if s[i]!=s[i+1]:
                    if count[int(s[i])]<now:
                        count[int(s[i])]=now
                    now=0
            else:
                if count[int(s[i])]<now:
                    count[int(s[i])]=now
        return count[1]>count[0]