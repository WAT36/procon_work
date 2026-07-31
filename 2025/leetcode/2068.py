class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        w1m={}
        w2m={}
        for i in range(len(word1)):
            if word1[i] in w1m.keys():
                w1m[word1[i]]=w1m[word1[i]]+1
            else:
                w1m[word1[i]]=1
        for i in range(len(word2)):
            if word2[i] in w2m.keys():
                w2m[word2[i]]=w2m[word2[i]]+1
            else:
                w2m[word2[i]]=1
        for k,v in w1m.items():
            if k in w2m:
                if abs(v - w2m[k])>3:
                    return False
            else:
                if v > 3:
                    return False
        for k,v in w2m.items():
            if k in w1m:
                if abs(v - w1m[k])>3:
                    return False
            else:
                if v > 3:
                    return False
        return True