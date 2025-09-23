# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # return [sum of tree,sum of tilt]
    def findTilt2(self, root: Optional[TreeNode]) -> [int]:
        if root is None:
            return [0,0]
        l=self.findTilt2(root.left)
        r=self.findTilt2(root.right)
        tilt=abs(l[0]-r[0])
        return [root.val+l[0]+r[0],tilt+l[1]+r[1]]

    def findTilt(self, root: Optional[TreeNode]) -> int:
        return self.findTilt2(root)[1]