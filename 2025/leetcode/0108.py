# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def divideArrayAndMakeTreeNode(self, arr: List[int]):
        if(arr is None or len(arr) == 0):
            return None
        elif(len(arr)==1):
            return TreeNode(val=arr[0],left=None,right=None)

        center_i = int((- ( -(len(arr)/2) // 1)) - 1)
        return TreeNode(val=arr[center_i],left=self.divideArrayAndMakeTreeNode(arr[:center_i]),right=self.divideArrayAndMakeTreeNode(arr[center_i+1:]))

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        sortedNum=sorted(nums)
        return self.divideArrayAndMakeTreeNode(arr=sortedNum)


        