class Solution:
    def removeAnagrams(self, words: list[str]) -> list[str]:
        ans=[words[0]]
        for i in range(len(words)):
            lasti=sorted(list(ans[-1]))
            wi=sorted(list(words[i]))
            if lasti!=wi:
                ans.append(words[i])
        return ans