class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=0
        now=0
        for gi in gain:
            now+=gi
            ans=max(ans,now)
        return ans