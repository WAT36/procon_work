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

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        l=self.treeNodeToList(root)
        print(l)
        l=sorted(list(set(l)))
        return l[1] if len(l)>=2 else -1