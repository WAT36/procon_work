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

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listnode=[]
        while head:
            listnode.append(head.val)
            head=head.next
        ans=[]
        for i in range(len(listnode)):
            if listnode.count(listnode[i]) == 1:
                ans.append(listnode[i])
        return self.listToListNode(ans)

        