class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.next = next
    
    def listToListNode(self, values: List[int]):
        if values is None or len(values) == 0:
            return None
        return ListNode(val=values[0],next=self.listToListNode(values=values[1:]))
    