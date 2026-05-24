class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ss=s.split(" ")
        ans=ss[:k]
        return " ".join(ans)