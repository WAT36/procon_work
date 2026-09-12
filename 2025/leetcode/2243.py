class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            si=[]
            while len(s)>k:
                si.append(s[:k])
                s=s[k:]
            if len(s)>0:
                si.append(s)
            
            sj=""
            for sii in si:
                sj=sj+str(sum([int(sii[k]) for k in range(len(sii))]))
            s=sj
        return s
