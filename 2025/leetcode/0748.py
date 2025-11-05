class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lp=sorted(list(licensePlate.lower()))
        ans=""
        ans_matched=0
        ans_len=9999999999
        matched=0
        for word in words:
            w=sorted(list(word))
            ind=-1
            for lpi in lp:
                if ind+1 < len(w) and lpi in w[ind+1:]:
                    ind=w.index(lpi,ind+1)
                    matched+=1
                    print('#',lpi,ind)
            print(word,matched,ans_matched,ans_len,ans)
            if matched > ans_matched or (matched == ans_matched and len(word) < ans_len):
                ans=word
                ans_matched=matched
                ans_len=len(word)
            matched=0
        return ans

