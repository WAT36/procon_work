class Solution:
    def minTimeToType(self, word: str) -> int:
        alpha="abcdefghijklmnopqrstuvwxyz"
        ans=len(word)
        word='a'+word
        for i in range(len(word)-1):
            w1=word[i]
            w2=word[i+1]
            if w1<w2:
                ans+=min(alpha.index(w2)-alpha.index(w1),alpha.index(w1)+26-alpha.index(w2))
            else:
                ans+=min(alpha.index(w1)-alpha.index(w2),alpha.index(w2)+26-alpha.index(w1))
        return ans
