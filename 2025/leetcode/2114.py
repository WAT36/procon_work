class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for s in sentences:
            ans=max(ans,len(s.split(' ')))
        return ans