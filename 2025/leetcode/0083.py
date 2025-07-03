# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def makeListNode(self, vals:[int]):
        if(len(vals)==0):
            return None
        return ListNode(val=vals[0],next=None if len(vals)<=1 else self.makeListNode(vals=vals[1:]))

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        sets=set()
        ansval=[]
        while head:
            if(head.val not in sets):
                sets.add(head.val)
                ansval.append(head.val)
            head=head.next
        return self.makeListNode(ansval)
        