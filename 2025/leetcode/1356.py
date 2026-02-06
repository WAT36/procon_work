class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bins=[[] for _ in range(len(bin(max(arr))))]
        for ai in arr:
            bins[list(bin(ai)).count('1')].append(ai)
        ans=[]
        for bi in bins:
            ans=ans+sorted(bi)
        return ans