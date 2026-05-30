class Solution:
    def replaceDigits(self, s: str) -> str:
        alpha='abcdefghijklmnopqrstuvwxyz'
        ss=list(s)
        i=1
        while i<len(s):
            ss[i]=alpha[(alpha.index(ss[i-1])+int(ss[i]))%len(alpha)]
            i+=2
        return ''.join(ss)