# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeNodeToArray(self, t:Optional[TreeNode]):
        if(t is None):
            return [None]
        leftList= [*self.treeNodeToArray(t.left)]
        rightList= [*self.treeNodeToArray(t.right)]
        return [t.val,*leftList,*rightList]

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        plist=self.treeNodeToArray(p)
        qlist=self.treeNodeToArray(q)
        if(len(plist) != len(qlist)):
            return False
        else:
            for i in range(len(plist)):
                if(plist[i] != qlist[i]):
                    return False
            return True
        