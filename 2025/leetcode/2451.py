class Solution:
    def oddString(self, words: list[str]) -> str:
        alpha="abcdefghijklmnopqrstuvwxyz"
        d=[]
        for w in words:
            wi=[]
            for i in range(len(w)-1):
                wi.append(alpha.index(w[i+1]) - alpha.index(w[i]))
            d.append(wi)
        for i in range(len(d)):
            if d.count(d[i])==1:
                return words[i]
        return -1