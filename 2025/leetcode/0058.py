import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(re.split(r' +',s.strip())[-1])