class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        now_depth=0
        for i in range(len(s)):
            if(s[i]=="("):
                now_depth+=1
            elif(s[i]==")"):
                now_depth-=1
            ans=max(ans,now_depth)
        return ans

