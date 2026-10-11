class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans=9999999999
        i=0
        while i+k<=len(blocks):
            ans=min(ans,blocks[i:i+k].count('W'))
            i+=1
        return ans