import collections
class Solution:
    def sortString(self, s: str) -> str:
        s=list(s)
        s_count=collections.Counter(s)

        ans=[]
        s_words=list(sorted(s_count.keys()))

        while(len(ans)<len(s)):
            for k in s_words:
                if(s_count[k]>0):
                    ans.append(k)
                    s_count[k]-=1

            for k in s_words[::-1]:
                if(s_count[k]>0):
                    ans.append(k)
                    s_count[k]-=1

        return ''.join(ans)
