class Solution:
    def maximumValue(self, strs: list[str]) -> int:
        ans=0
        for s in strs:
            try:
                ansi=int(s)
                ans=max(ans,ansi)
            except:
                ansi=len(s)
                ans=max(ans,ansi)
        return ans
