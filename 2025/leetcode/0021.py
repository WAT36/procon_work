# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def makeListNode(self, mergedList: [int]) -> Optional[ListNode]:
        return ListNode(val=mergedList[0],next=None if len(mergedList) <= 1 else self.makeListNode(mergedList[1:]))

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list=[]
        while(list1):
            merged_list.append(list1.val)
            list1 = list1.next

        while(list2):
            merged_list.append(list2.val)
            list2 = list2.next

        merged_list.sort()
        if len(merged_list) == 0:
            return None    
        return self.makeListNode(merged_list)
        