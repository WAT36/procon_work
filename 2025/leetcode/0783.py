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

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        l=self.treeNodeToList(root)
        l.sort()
        ans=9999999999999
        for i in range(len(l)-1):
            ans=min(ans,l[i+1]-l[i])
        return ans
        