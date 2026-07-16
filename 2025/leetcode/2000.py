class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        chind=word.index(ch)
        return word[0:chind+1][::-1]+word[chind+1:]