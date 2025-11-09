class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alpha="abcdefghijklmnopqrstuvwxyz"
        ans=[0,0]
        ansi=0
        for si in s:
            wi=widths[alpha.index(si)]
            if ansi+wi <= 100:
                ansi+=wi
            else:
                ans[0]=ans[0]+1
                ansi=wi
        else:
            ans[0]=ans[0]+1
            ans[1]=ansi
        return ans
