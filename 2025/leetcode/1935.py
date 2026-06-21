class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans=0
        texts=text.split(' ')
        for t in texts:
            for i in range(len(brokenLetters)):
                if brokenLetters[i] in t:
                    ans+=1
                    break
        return len(texts)-ans