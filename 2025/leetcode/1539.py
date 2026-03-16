class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans=0
        count=0
        while count<k:
            ans+=1
            if ans not in arr:
                count+=1
        return ans