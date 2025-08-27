class Solution:
    def longestPalindrome(self, s: str) -> int:
        m={}
        for i in range(len(s)):
            if s[i] not in m:
                m[s[i]] = 1
            else:
                num=m[s[i]]
                m[s[i]] = num+1
        oddFlag=False
        ans=0
        for val in m.values():
            if val % 2 == 0:
                ans+=val
            else:
                oddFlag=True
                ans+=(val-1)
        if oddFlag:
            ans+=1
        return ans
        