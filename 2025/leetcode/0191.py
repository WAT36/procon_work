class Solution:
    def hammingWeight(self, n: int) -> int:
        return list(bin(n)[2:]).count('1')