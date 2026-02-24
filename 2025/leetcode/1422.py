class Solution:
    def maxScore(self, s: str) -> int:
        ans=0
        left=0
        right=s.count("1")
        for i in range(len(s)-1):
            if s[i]=="0":
                left+=1
            elif s[i]=="1":
                right-=1
            if ans<left+right:
                ans=left+right
            #print(i,left,right,ans)
        return ans
