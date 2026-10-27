class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        if (event1[1]>=event2[0] and event1[0]<=event2[1]) or (event1[0]<=event2[1] and event1[1]>=event2[0]):
            return True
        return False