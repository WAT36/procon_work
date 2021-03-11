class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        l=[[indices[i],s[i]] for i in range(len(s))]
        l.sort()
        lstr=[l[i][1] for i in range(len(s))]
        return ''.join(lstr)