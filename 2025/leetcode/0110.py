# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isHeightBalanced(self,tree: Optional[TreeNode]) -> [int,bool]:
        if(tree is None):
            return [0,True]
        leftResult = self.isHeightBalanced(tree.left)
        rightResult = self.isHeightBalanced(tree.right)
        result = False
        if abs(leftResult[0] - rightResult[0]) <= 1:
            result = True and leftResult[1] and rightResult[1]
        #print(tree.val,leftResult,rightResult)
        return [max(leftResult[0],rightResult[0])+1,result]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.isHeightBalanced(root))[1]