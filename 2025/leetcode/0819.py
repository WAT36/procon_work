import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words=re.split(r'[\!\?\'\,\;\.\ ]', paragraph)
        print(words)
        m={}
        for w in words:
            wlow=w.lower()
            if wlow in banned or w == "":
                continue
            elif wlow in m.keys():
                v=m[wlow]
                m[wlow]=v+1
            else:
                m[wlow]=1
        ansv=0
        ansk=""
        for k,v in m.items():
            if ansv<v:
                ansv=v
                ansk=k
        return ansk