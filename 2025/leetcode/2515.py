class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        ans=99999999999
        ind=[]
        i=0
        while target in words[i:]:
            indi=words.index(target,i)
            ind.append(indi)
            ind.append(indi-len(words))
            ind.append(indi+len(words))
            i=indi+1
        for i in ind:
            ans=min(ans,abs(i-startIndex))
        #print(ind)
        return ans
