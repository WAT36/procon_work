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
        leftList= [*self.treeNodeToList(t.left)]
        rightList= [*self.treeNodeToList(t.right)]
        return [t.val,*leftList,*rightList]
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l=self.treeNodeToList(root)
        l.sort()
        for i in range(len(l)-1):
            if i >= len(l):
                break
            if k-l[i] in l[i+1:]:
                return True
        return False