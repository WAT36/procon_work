class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumalice=sum(aliceSizes)
        sumbob=sum(bobSizes)
        for a in aliceSizes:
            b2=sumbob-sumalice+(a*2)
            if b2 % 2 != 0:
                continue
            b=b2//2
            if b in bobSizes:
                return [a,b]
        return []