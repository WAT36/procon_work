# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return 1 + self.countNodes(root.right)
        elif root.right is None:
            return 1 + self.countNodes(root.left)
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        