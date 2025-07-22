# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None):
            return None
        valList=[]
        while head:
            valList.append(head.val)
            head=head.next
        valList=valList[::-1]
        ansList=ListNode()
        ansHead=ansList
        for i in range(len(valList)):
            ansHead.val=valList[i]
            ansHead.next=ListNode() if i!=len(valList)-1 else None
            ansHead=ansHead.next
        return ansList
        
        