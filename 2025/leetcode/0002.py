# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def makeListNode(self,strnum: string) -> Optional[ListNode]:
        return ListNode(val=int(strnum[0]),next=None if len(strnum) <= 1 else self.makeListNode(strnum[1:]))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        strl1=""
        while(l1):
            strl1 = str(l1.val) + strl1
            l1 = l1.next

        strl2=""
        while(l2):
            strl2 = str(l2.val) + strl2
            l2 = l2.next
        
        ans = str(int(strl1) + int(strl2))[::-1]
        return self.makeListNode(ans)


        