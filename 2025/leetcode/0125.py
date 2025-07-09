import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=re.sub(r'[^a-z0-9]','',s.lower())
        return t == t[::-1]