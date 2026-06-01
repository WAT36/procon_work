class Solution:
    def sortSentence(self, s: str) -> str:
        ss=s.split(" ")
        ans=[""  for _ in range(len(ss)+1)]
        for si in ss:
            ind=int(si[-1])
            ans[ind]=si[:-1]
        return " ".join(ans)[1:]
