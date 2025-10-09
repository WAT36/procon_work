# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels2(self, root: Optional[TreeNode], level:int) -> List[[int]]:
        if root is None:
            return []
        left=self.averageOfLevels2(root.left,level+1)
        right=self.averageOfLevels2(root.right,level+1)
        val=[root.val,level]
        return [val]+left+right

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        vals=self.averageOfLevels2(root,0)
        maxind=max([vals[i][1] for i in range(len(vals))])
        sumval=[[0,0] for i in range(maxind+1)]
        #print(vals)
        #print(sumval)
        for val in vals:
            vi=sumval[val[1]]
            vi[0]+=val[0]
            vi[1]+=1
            sumval[val[1]]=vi
        #print(sumval)
        ans=[]
        for sv in sumval:
            ans.append(sv[0]/sv[1])
        return ans


