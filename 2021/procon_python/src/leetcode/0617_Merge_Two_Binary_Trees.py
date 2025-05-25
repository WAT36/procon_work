# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,t1:TreeNode,t2:TreeNode):
        if(t1==None and t2==None):
            return None
        elif(t1==None):
            t=TreeNode(t2.val)
            t.left=self.dfs(None,t2.left)
            t.right=self.dfs(None,t2.right)
            return t
        elif(t2==None):
            t=TreeNode(t1.val)
            t.left=self.dfs(t1.left,None)
            t.right=self.dfs(t1.right,None)
            return t
        else:
            t=TreeNode(t1.val+t2.val)
            t.left=self.dfs(t1.left,t2.left)
            t.right=self.dfs(t1.right,t2.right)
            return t

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t=self.dfs(t1,t2)
        return t


