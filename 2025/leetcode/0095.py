# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(lo: int, hi: int) -> List[Optional[TreeNode]]:
            if lo > hi:
                return [None]
            res: List[Optional[TreeNode]] = []
            for root_val in range(lo, hi + 1):
                for left in build(lo, root_val - 1):
                    for right in build(root_val + 1, hi):
                        node = TreeNode(root_val)
                        node.left = left
                        node.right = right
                        res.append(node)
            return res

        return build(1, n)