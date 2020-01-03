# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root: TreeNode, val: int):
        if(root.val==val):
            return root
        elif(val < root.val):
            if(root.left==None):
                return None
            else:
                return self.dfs(root.left,val)
        else:
            if(root.right==None):
                return None
            else:
                return self.dfs(root.right,val)



    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.dfs(root,val)


