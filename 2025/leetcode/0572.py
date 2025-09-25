# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeNodeToList(self, t:Optional[TreeNode]):
        if(t is None):
            return [None]
        leftList= [*self.treeNodeToList(t.left)]
        rightList= [*self.treeNodeToList(t.right)]
        return [t.val,*leftList,*rightList]

    def checkNodeList(self, t:Optional[TreeNode],ans:[int]) -> bool:
        if t is None:
            return False
        tlist=self.treeNodeToList(t)
        if tlist == ans:
            return True
        left=self.checkNodeList(t.left,ans)
        right=self.checkNodeList(t.right,ans)
        return left or right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subRootlist=self.treeNodeToList(subRoot)
        return self.checkNodeList(root,subRootlist)

