class Solution:
    def isCharacter(self, bits: List[int]) -> bool:
        print(bits)
        if len(bits) == 0:
            return True
        elif len(bits) == 1:
            if bits[-1] == 0:
                return True
            else:
                return False
        elif bits[-1] == 0:
            if bits[-2] == 0:
                return self.isCharacter(bits[:-1])
            elif bits[-2] == 1:
                return self.isCharacter(bits[:-1]) or self.isCharacter(bits[:-2])
        elif bits[-1] == 1:
            if bits[-2] == 0:
                return False
            elif bits[-2] == 1:
                return self.isCharacter(bits[:-2])

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        return self.isCharacter(bits[:-1])
        