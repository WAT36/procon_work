class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        j1=''.join(word1)
        j2=''.join(word2)
        return j1 == j2