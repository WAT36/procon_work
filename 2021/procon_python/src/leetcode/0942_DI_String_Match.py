#解説見ちった..
class Solution:
    def diStringMatch(self, S: str) -> list[int]:
        a=[i for i in range(len(S)+1)]
        ans=[]
        for i in range(len(S)):
            if(S[i]=='I'):
                ans.append(a[0])
                a.pop(0)
            else:
                ans.append(a.pop())
        ans.append(a.pop())
        return ans
