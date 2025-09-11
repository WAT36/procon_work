# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def listVal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans=[]
        ans+=self.listVal(root.left)
        ans+=self.listVal(root.right)
        ans+=[root.val]
        return ans

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        vals=self.listVal(root)
        setval=list(set(vals))
        counts={}
        for vi in setval:
            counts[vi]=vals.count(vi)
        maxval = max(counts.values())
        ans=[]
        for k,v in counts.items():
            if v==maxval:
                ans.append(k)
        return ans