class Solution:
    def similarPairs(self, words: list[str]) -> int:
        ans=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if sorted(list(set(list(words[i])))) == sorted(list(set(list(words[j])))):
                    ans+=1
                    #print(words[i],words[j])
        return ans