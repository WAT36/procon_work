# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #[diameter,mmaxDepth,maxdiameter]を返す
    def calcDepth(self, root: Optional[TreeNode]) -> [int]:
        if root is None:
            return [0,-1,0]
        leftresult=self.calcDepth(root.left)
        rightresult=self.calcDepth(root.right)
        diameter=leftresult[1]+rightresult[1]+2
        #print(root.val,diameter,leftresult,rightresult)
        return [diameter,max(leftresult[1],rightresult[1])+1,max(leftresult[2],rightresult[2],diameter)]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.calcDepth(root)[2]
        
