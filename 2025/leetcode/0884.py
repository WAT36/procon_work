class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans=[]
        s1s=s1.split(" ")
        s2s=s2.split(" ")
        for s in s1s:
            if s1s.count(s) == 1 and s not in s2s:
                ans.append(s)

        for s in s2s:
            if s2s.count(s) == 1 and s not in s1s:
                ans.append(s)
        return ans