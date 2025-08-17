import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        result = re.fullmatch(p, s)
        if result is None:
            return False
        return True