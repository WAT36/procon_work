from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumofGrandChild(self,root: TreeNode):
        ans=0
        if(root.val%2==0):
            if(root.left!=None):
                leftchild=root.left
                if(leftchild.left!=None):
                    ans+=leftchild.left.val
                if(leftchild.right!=None):
                    ans+=leftchild.right.val
            if(root.right!=None):
                rightchild=root.right
                if(rightchild.left!=None):
                    ans+=rightchild.left.val
                if(rightchild.right!=None):
                    ans+=rightchild.right.val
        return ans

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q=deque()
        q.append(root)
        ans=0
        while(len(q)>0):
            node=q.popleft()
            ans+=self.sumofGrandChild(node)
            if(node.left!=None):
                q.append(node.left)
            if(node.right!=None):
                q.append(node.right)
        return ans