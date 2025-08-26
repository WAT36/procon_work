# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return (root.left.val if root.left is not None and root.left.left is None and root.left.right is None else 0) + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        