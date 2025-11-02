import bisect
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lfirst=letters[0]
        letters.sort()
        ind=bisect.bisect_right(letters,target)
        if ind >= len(letters):
            return lfirst
        return letters[ind]