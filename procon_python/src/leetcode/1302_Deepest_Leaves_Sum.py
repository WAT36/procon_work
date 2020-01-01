# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,level,root):
        ans=[]
        if(root.left == None and root.right == None):
            ans.append([level,root.val])
        if(root.left != None):
            ans.extend(self.dfs(level+1,root.left))
        if(root.right != None):
            ans.extend(self.dfs(level+1,root.right))
        return ans


    def deepestLeavesSum(self, root: TreeNode) -> int:
        ans=self.dfs(0,root)
        ans.sort(reverse=True)
        maxlevel=ans[0][0]
        anssum=0
        for i in range(len(ans)):
            if(ans[i][0]==maxlevel):
                anssum+=ans[i][1]
            else:
                break
        return anssum
