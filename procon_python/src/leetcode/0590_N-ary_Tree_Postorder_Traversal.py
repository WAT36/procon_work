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
        elif(root.children == None):
            ans.append(root.val)
            return ans
        else:
            child=root.children
            for i in range(len(child)):
                ans.extend(self.dfs(child[i],[]))
            ans.append(root.val)
            return ans

    def postorder(self, root: 'Node') -> List[int]:
        ans=[]
        self.dfs(root,ans)
        return ans

