# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcSum(self,root: Optional[TreeNode]) -> [int]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        arr = [*self.calcSum(root.left), *self.calcSum(root.right)]
        return [arr[i]+root.val for i in range(len(arr))]

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        arr = self.calcSum(root)
        return targetSum in arr