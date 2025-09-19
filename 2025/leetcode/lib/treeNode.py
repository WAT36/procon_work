# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # treeNodeをListにする
    def treeNodeToList(self, t:Optional[TreeNode]):
        if(t is None):
            return []
        leftList= [*self.treeNodeToList(t.left)]
        rightList= [*self.treeNodeToList(t.right)]
        return [t.val,*leftList,*rightList]

    # bfs版、iの子が2i+1,2i+2に入る
    from collections import deque
    def treeNodeToList(self, t:Optional[TreeNode]):
        #bfs
        ans=[]
        queue=deque([t])
        while len(queue)>0:
            node=queue.popleft()
            ans.append(node.val if node is not None else None)
            if(node is not None):
                queue.append(node.left)
                queue.append(node.right)
        return ans
    
    # 左右逆にしたTreeNodeを返す（0226）
    def makeInverseTreeNode(self,root: Optional[TreeNode]):
        if root is None:
            return None
        return TreeNode(val=root.val,left=self.makeInverseTreeNode(root=root.right),right=self.makeInverseTreeNode(root=root.left))