# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcMinDepth(self, root:Optional[TreeNode]) -> int:
        if(root is None):
            return 0
        calcLeft=self.calcMinDepth(root.left)
        calcRight=self.calcMinDepth(root.right)
        if(calcLeft == 0 and calcRight == 0):
            return 1
        elif(calcLeft==0):
            return calcRight+1
        elif(calcRight==0):
            return calcLeft+1
        else:
            return min(calcLeft,calcRight)+1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.calcMinDepth(root)