class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans=""
        while columnNumber > 0:
            sur = columnNumber % 26
            ans = ALPHABET[sur-1] + ans
            if columnNumber % 26 != 0:
                columnNumber //= 26
            else:
                columnNumber //= 26
                columnNumber -= 1
        return ans
        