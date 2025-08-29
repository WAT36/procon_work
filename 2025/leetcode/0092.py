# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listToListNode(self, values: List[int]):
        if values is None or len(values) == 0:
            return None
        return ListNode(val=values[0],next=self.listToListNode(values=values[1:]))

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        listnode=[]
        while head:
            listnode.append(head.val)
            head=head.next
        ans=listnode[:left-1] + listnode[left-1:right][::-1] + listnode[right:]
        return self.listToListNode(ans)