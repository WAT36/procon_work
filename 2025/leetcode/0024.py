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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[]
        while head:
            values.append(head.val)
            head = head.next
        swappedList=[]
        i=0
        while i < len(values):
            if i+1 < len(values):
                swappedList.append(values[i+1])
            swappedList.append(values[i])
            i+=2 
        return self.listToListNode(values=swappedList)
