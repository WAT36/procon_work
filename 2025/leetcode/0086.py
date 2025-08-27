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

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        listnode=[]
        while head:
            listnode.append(head.val)
            head=head.next
        flag=True
        while flag:
            flag=False
            for i in range(len(listnode)-1):
                if listnode[i] >= x and listnode[i+1] < x:
                    swap = listnode[i]
                    listnode[i] = listnode[i+1]
                    listnode[i+1] = swap
                    flag=True
        return self.listToListNode(listnode)