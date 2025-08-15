class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        swap = s[::-1]
        for i in range(len(s)):
            s[i] = swap[i]
        