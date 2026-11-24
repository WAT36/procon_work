class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            maxg=max(gifts)
            rootg=int(math.sqrt(maxg))
            maxi=gifts.index(maxg)
            gifts[maxi]=rootg
        return sum(gifts)
