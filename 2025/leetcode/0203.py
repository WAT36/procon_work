# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans=None
        ansNow=None
        while head:
            if(head.val != val):
                if ans is None:
                    ans=ListNode(val=head.val)
                    ansNow=ans
                else:
                    ansNow.next=ListNode(head.val)
                    ansNow=ansNow.next
            head=head.next
        return ans
                

