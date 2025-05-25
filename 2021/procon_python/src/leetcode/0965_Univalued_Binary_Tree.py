# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,root:TreeNode,val:int):
        if(root==None):
            return True
        elif(root.val==val):
            return self.dfs(root.left,root.val) and self.dfs(root.right,root.val)
        else:
            return False


    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.dfs(root,root.val)