"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def dfs(self,root:'Node',depth: int):
        if(root==None or root.children==None):
            return depth
        else:
            maxdepth=depth
            child=root.children
            for c in child:
                maxdepth=max(maxdepth,self.dfs(c,depth+1))
            return maxdepth

    def maxDepth(self, root: 'Node') -> int:
        if(root==None):
            return 0
        else:
            return self.dfs(root,1)

