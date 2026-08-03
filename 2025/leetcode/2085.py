class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ans1=[]
        for w in words1:
            if words1.count(w)==1:
                ans1.append(w)
        ans2=[]
        for w in ans1:
            if words2.count(w)==1:
                ans2.append(w)
        return len(ans2)