class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for wi in words:
            for wj in words:
                if wi == wj:
                    continue
                elif wi in wj:
                    ans.append(wi)
                    break
        return ans