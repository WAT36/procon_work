class Solution:
    def wordCount(self,word):
        list_word=list(word)
        set_chr=list(set(word))
        d={}
        for c in set_chr:
            d[c]=list_word.count(c)
#        print(d)
        return d

    def countCharacters(self, words: list[str], chars: str) -> int:
        d_chars=self.wordCount(chars)
        ans=0
        for w in words:
            d_w=self.wordCount(w)
            for wi in d_w.keys():
                if(d_chars.get(wi,0) < d_w[wi]):
                    break
            else:
                ans+=len(w)

        return ans