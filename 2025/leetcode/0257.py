# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [str(root.val)]
        ans=[]        
        if root.left is not None:
            ans.extend(self.binaryTreePaths(root=root.left))
        if root.right is not None:
            ans.extend(self.binaryTreePaths(root=root.right))
        for i in range(len(ans)):
            ans[i] = str(root.val) + "->" + ans[i]
        return  ans
