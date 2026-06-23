class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha=list('*abcdefghijklmnopqrstuvwxyz')
        t=""
        for i in range(len(s)):
            t+=str(alpha.index(s[i]))
        for _ in range(k):
            ansi=0
            for i in range(len(t)):
                ansi+=int(t[i])
            t=str(ansi)
        return int(t)