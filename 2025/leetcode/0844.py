class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sq=[]
        tq=[]
        for i in range(len(s)):
            if s[i] == '#':
                if len(sq) > 0:
                    sq.pop()
            else:
                sq.append(s[i])

        for i in range(len(t)):
            if t[i] == '#':
                if len(tq) > 0:
                    tq.pop()
            else:
                tq.append(t[i])
        return ''.join(sq) == ''.join(tq)