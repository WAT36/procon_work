class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alpha)):
            if alpha[i] not in sentence:
                return False
        return True