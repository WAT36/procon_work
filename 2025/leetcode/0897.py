# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeNodeToList(self,root: Optional[TreeNode]) -> [int]:
        if root is None:
            return []
        return [*self.treeNodeToList(root.left),root.val,*self.treeNodeToList(root.right)]

    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l=self.treeNodeToList(root)
        rinit=TreeNode()
        r=rinit
        for i in range(len(l)-1):
            r.val=l[i]
            r.right=TreeNode()
            r=r.right
        r.val=l[-1]
        return rinit