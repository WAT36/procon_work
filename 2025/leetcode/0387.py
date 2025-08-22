class Solution:
    def firstUniqChar(self, s: str) -> int:
        sletter=list(set(list(s)))
        slettermap={}
        s_unique=[]
        for i in range(len(sletter)):
            slettermap[sletter[i]] = list(s).count(sletter[i])
            if slettermap[sletter[i]] == 1:
                s_unique.append(sletter[i])
        
        if len(s_unique) == 0:
            return -1
        else:
            ans=999999999
            for i in range(len(s_unique)):
                ans=min(ans,list(s).index(s_unique[i]))
            return ans