class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans=[]
        for s in arr:
            if arr.count(s)==1:
                ans.append(s)
        return ans[k-1] if k<=len(ans) else ""