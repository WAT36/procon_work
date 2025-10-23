class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binn=bin(n)[2:]
        for i in range(len(binn)-1):
            if binn[i] == binn[i+1]:
                return False
        return True