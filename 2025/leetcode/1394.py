class Solution:
    def findLucky(self, arr: List[int]) -> int:
        numset=set([])
        ansset=set([])
        for ai in arr:
            if ai not in numset:
                if arr.count(ai) == ai:
                    ansset.add(ai)
                numset.add(ai)
        return max(list(ansset)) if len(list(ansset))>0 else -1