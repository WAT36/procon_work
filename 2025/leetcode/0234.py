# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        while head:
            vals.append(head.val)
            head = head.next
        reversed_vals=vals[::-1]
        return vals == reversed_vals
