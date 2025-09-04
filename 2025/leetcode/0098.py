# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST2(self, root: Optional[TreeNode], minnum:int, maxnum:int) -> bool:
        #print(root.val if root is not None else None,minnum,maxnum)
        if root is None:
            return True
        if root.val <= minnum or maxnum <= root.val:
            return False
        if root.left is None and root.right is None:
            return True
        if root.left is not None and root.left.val >= root.val:
            return False
        if root.right is not None and root.right.val <= root.val:
            return False
        return self.isValidBST2(root.left,minnum,min(maxnum,root.val)) and self.isValidBST2(root.right,max(minnum,root.val),maxnum)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBST2(root,-2 ** 32,2 **32)