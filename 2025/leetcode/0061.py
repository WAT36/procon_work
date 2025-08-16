# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listNodeToList(self, head: Optional[ListNode]):
        if head is None:
            return []
        ans=[head.val]
        l=self.listNodeToList(head.next)
        ans.extend(l)
        return ans

    def listToListNode(self, values: List[int]):
        if values is None or len(values) == 0:
            return None
        return ListNode(val=values[0],next=self.listToListNode(values=values[1:]))

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = self.listNodeToList(head)
        if len(l)==0:
            return None
        k=k%len(l)
        rotatedl = l[-k:] + l[:-k]
        return self.listToListNode(rotatedl)