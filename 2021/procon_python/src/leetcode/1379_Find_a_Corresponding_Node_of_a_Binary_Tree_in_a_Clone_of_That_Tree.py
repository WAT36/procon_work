# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:

    ans_node=None

    def dfs(self,node,target):
        if(node.val==target.val):
            self.ans_node=node
            return True

        if(node.left is not None and self.dfs(node.left,target)):
            return True

        if(node.right is not None and self.dfs(node.right,target)):
            return True

        return False

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.dfs(cloned,target)
        return self.ans_node