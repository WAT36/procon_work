class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binn=bin(n)[2:]
        binn=binn.replace('0','*')
        binn=binn.replace('1','0')
        binn=binn.replace('*','1')
        return int(binn,2)