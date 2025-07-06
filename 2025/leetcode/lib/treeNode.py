# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # treeNodeをListにする
    def treeNodeToList(self, t:Optional[TreeNode]):
        if(t is None):
            return [None]
        leftList= [*self.treeNodeToList(t.left)]
        rightList= [*self.treeNodeToList(t.right)]
        return [t.val,*leftList,*rightList]