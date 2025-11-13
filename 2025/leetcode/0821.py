class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l=[99999 for _ in range(len(s))]
        r=[99999 for _ in range(len(s))]
        ans=[99999 for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] == c:
                l[i] = 0
            elif i>0:
                l[i] = l[i-1]+1

        for i in range(len(s)-1,-1,-1):
            if s[i] == c:
                r[i] = 0
            elif i<len(s)-1:
                r[i] = r[i+1]+1
        # print(l)
        # print(r)
        for i in range(len(s)):
            ans[i]=min(l[i],r[i])
        return ans

