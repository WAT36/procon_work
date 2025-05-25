"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def dfs(self, root, ans):
        if(root == None):
            return []
        else:
            ans.append(root.val)
            if(root.children == None):
                return ans
            else:
                child=root.children
                for i in range(len(child)):
                    ans=self.dfs(child[i],ans)
                return ans

    def preorder(self, root: 'Node') -> List[int]:
        ans=[]
        self.dfs(root,ans)
        return ans