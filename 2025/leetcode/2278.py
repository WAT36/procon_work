class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c=list(s).count(letter)
        return int((100*c/len(s))//1)