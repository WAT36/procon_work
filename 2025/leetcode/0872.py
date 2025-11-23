# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeNodeToList(self, t:Optional[TreeNode]):
        if(t is None):
            return []
        elif(t.left is None and t.right is None):
            return [t.val]
        leftList= [*self.treeNodeToList(t.left)]
        rightList= [*self.treeNodeToList(t.right)]
        return [*leftList,*rightList]

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1leaf=self.treeNodeToList(root1)
        r2leaf=self.treeNodeToList(root2)
        return r1leaf == r2leaf
