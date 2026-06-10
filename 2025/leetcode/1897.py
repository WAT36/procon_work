class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words)==1:
            return True
        wmap={}
        for w in words:
            for i  in range(len(w)):
                if w[i] in wmap:
                    wmap[w[i]]=wmap[w[i]]+1
                else:
                    wmap[w[i]]=1
        #  print(wmap)
        for k,v in wmap.items():
            if v%len(words)!=0:
                return False
        return True