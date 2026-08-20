class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        i=0
        ans=[]
        while i<len(s):
            ans.append(s[i:i+k] if i+k<=len(s) else (s[i:]+(fill * k))[:k])
            i+=k
        return ans