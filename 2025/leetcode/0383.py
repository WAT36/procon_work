class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rletter=set(list(ransomNote))
        mletter=set(list(magazine))
        rlist=list(rletter)
        mlist=list(mletter)

        rmap={}
        mmap={}
        for i in range(len(mlist)):
            mmap[mlist[i]] = list(magazine).count(mlist[i])

        for i in range(len(rlist)):
            rmap[rlist[i]] = list(ransomNote).count(rlist[i])
            if rmap[rlist[i]] > mmap.get(rlist[i],0):
                return False
        return True

