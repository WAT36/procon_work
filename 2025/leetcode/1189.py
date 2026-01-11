class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        textlist=list(text)
        words=["b","a","l","l","o","o","n"]
        ans=0
        i=0
        while True:
            if words[i] not in textlist:
                break
            else:
                textlist.remove(words[i])
                i+=1
            if i>=len(words):
                ans+=1
                i=0
        return ans