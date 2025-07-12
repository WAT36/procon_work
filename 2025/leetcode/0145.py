# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrder(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [*self.postOrder(root=root.left),*self.postOrder(root=root.right),root.val]

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postOrder(root=root)