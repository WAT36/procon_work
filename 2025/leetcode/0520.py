class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            return True
        elif word == word.lower():
            return True
        elif len(word) > 1 and (word[0] == word[0].upper() and word[1:] == word[1:].lower()):
            return True
        else:
            return False
        