class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row=['qwertyuiop','asdfghjkl','zxcvbnm']
        ans=[]
        for w in words:
            wl=w.lower()
            wiind=[]
            for wi in wl:
                for r in row:
                    if wi in r:
                        wiind.append(row.index(r))
            if len(list(set(wiind))) == 1:
                ans.append(w)
        return ans
