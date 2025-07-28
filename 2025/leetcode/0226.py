# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeInverseTreeNode(self,root: Optional[TreeNode]):
        if root is None:
            return None
        return TreeNode(val=root.val,left=self.makeInverseTreeNode(root=root.right),right=self.makeInverseTreeNode(root=root.left))

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.makeInverseTreeNode(root=root)