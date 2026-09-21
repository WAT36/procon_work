class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        ans=999999999
        for i in range(len(target)):
            ti=target[i]
            tc=target.count(ti)
            sc=s.count(ti)
            ansi=sc//tc
            ans=min(ans,ansi)
        return ans

