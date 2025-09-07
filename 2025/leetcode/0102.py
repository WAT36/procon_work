# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[[root.val]]
        left=self.levelOrder(root.left)
        right=self.levelOrder(root.right)
        anschild=[]
        for i in range(max(len(left),len(right))):
            li=[]
            if i < len(left):
                li=left[i]
            ri=[]
            if i < len(right):
                ri=right[i]
            anschild.append(li+ri)
        return ans + anschild