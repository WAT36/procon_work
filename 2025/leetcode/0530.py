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

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals=self.treeNodeToList(root)
        vals.sort()
        ans=999999999
        for i in range(1,len(vals)):
            ans=min(ans,vals[i]-vals[i-1])
        return ans


        