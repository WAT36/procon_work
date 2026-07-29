class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        v=["a","e","i","o","u"]
        ans=0
        for i in range(len(word)):
            if word[i] not in v:
                continue
            for j in range(i+1,len(word)):
                if word[j] not in v:
                    break
                for vi in v:
                    if vi not in word[i:j+1]:
                        break
                else:
                    #print(word[i:j+1])
                    ans+=1
        return ans