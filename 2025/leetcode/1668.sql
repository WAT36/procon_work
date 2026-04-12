class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        i=1
        while True:
            if (word*i) in sequence:
                i+=1
            else:
                return i-1
