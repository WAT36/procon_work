# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointers=[]
        pointer = head
        length=0
        while pointer:
            pointers.append(pointer)
            pointer = pointer.next
            length+=1
        removePointer = pointers[(-1*n)]

        if(n==length):
            head = head.next
        else:
            pointer = head
            while pointer:
                if(pointer.next == removePointer):
                    pointer.next = removePointer.next
                pointer = pointer.next
        return head
