class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        words=list(s.split())
        for i in words:
            ans+=''.join(list(reversed(list(i))))
            ans+=' '
        ans=ans[:-1]
        return ans