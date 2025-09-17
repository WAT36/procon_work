# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode], level: int = 0) -> List[List[int]]:
        if root is None:
            return []
        ans=[[root.val]]
        leftarr=self.zigzagLevelOrder(root.left,level+1)
        rightarr=self.zigzagLevelOrder(root.right,level+1)
        anslatter=[]
        for i in range(max(len(leftarr),len(rightarr))):
            leftarri=leftarr[i] if i < len(leftarr) else []
            rightarri=rightarr[i] if i < len(rightarr) else []
            ansi=(leftarri + rightarri)
            if len(ansi) > 0:
                anslatter.append(ansi)
        ans = ans + anslatter

        if level==0:
            for i in range(len(ans)):
                if i%2!=0:
                    ans[i]=ans[i][::-1]
        return ans



