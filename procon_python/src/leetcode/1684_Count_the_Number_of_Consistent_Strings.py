class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_word=set(list(allowed))
        ans=0

        for wi in words:
            wi_lists=list(set(list(wi)))
            flag=True
            for wili in wi_lists:
                if(wili not in allowed_word):
                    flag=False
                    break

            if(flag):
                ans+=1
        return ans