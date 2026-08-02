class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans=0
        for i in range(len(colors)):
            a=0
            while a<i:
                if colors[a]!=colors[i]:
                    if ans<abs(a-i):
                        ans=abs(a-i)
                    break
                a+=1
            a=len(colors)-1
            while i<a:
                if colors[a]!=colors[i]:
                    if ans<abs(a-i):
                        ans=abs(a-i)
                    break
                a-=1
        return ans