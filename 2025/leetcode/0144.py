# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val, *self.preOrder(root=root.left), *self.preOrder(root=root.right)]

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.preOrder(root=root)
        