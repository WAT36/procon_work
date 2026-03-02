class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split(' ')
        for i in range(len(words)):
            if searchWord == words[i][:len(searchWord)]:
                return i+1
        return -1