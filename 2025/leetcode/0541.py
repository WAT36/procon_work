class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=""
        i=0
        while i<len(s):
            ans+=(s[i:min(i+k,len(s))][::-1])
            if i+k<len(s):
                ans+=(s[i+k:min(i+2*k,len(s))])
            i+=(k+k)
        return ans