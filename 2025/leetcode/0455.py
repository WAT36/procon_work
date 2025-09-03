class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans=0
        j=0
        for i in range(len(g)):
            while True:
                if j>=len(s):
                    return ans
                if s[j]>=g[i]:
                    ans+=1
                    j+=1
                    break
                else:
                    j+=1
        return ans