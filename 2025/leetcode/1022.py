# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binlist(self, root: Optional[TreeNode]) -> [str]:
        if root is None:
            return []
        left=self.binlist(root.left)
        right=self.binlist(root.right)
        child=left + right
        #print(root.val,child)
        ans=[]
        for c in child:
            ans.append(str(root.val)+c)
        if len(ans)==0:
            ans.append(str(root.val))
        return ans

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        bins=self.binlist(root)
        #print(bins)
        ans=0
        for b in bins:
            #print(b,int(b,2))
            ans+=int(b,2)
        return ans
        