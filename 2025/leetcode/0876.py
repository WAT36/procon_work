# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heads=[]
        while head is not None:
            heads.append(head)
            head=head.next
        i=len(heads)//2
        return heads[i]