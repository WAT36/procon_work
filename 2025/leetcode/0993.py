# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def makeDepthList(self,root: Optional[TreeNode], x: int, y: int) -> [[int]]:
        if root is None:
            return []
        if (root.left is not None and root.right is not None) and ((root.left.val == x and root.right.val == y) or (root.left.val == y and root.right.val == x)):
            return None
        left=self.makeDepthList(root.left,x,y)
        right=self.makeDepthList(root.right,x,y)
        if left is None or right is None:
            return None
        ans=[[root.val]]
        for i in range(max(len(left),len(right))):
            ansi=[]
            if i<len(left):
                ansi=ansi+left[i]
            if i<len(right):
                ansi=ansi+right[i]
            ans.append(ansi)
            print(ans)
        return ans

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        l=self.makeDepthList(root,x,y)
        if l is None:
            return False
        print(l)
        for li in l:
            if x in li and y in li:
                return True
        return False