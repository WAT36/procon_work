# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if(root==None):
            return 0
        else:
            ans=0
            ans+=root.val if (L <= root.val and root.val <= R) else 0
            ans+=self.rangeSumBST(root.left,L,R)
            ans+=self.rangeSumBST(root.right,L,R)
            return ans

