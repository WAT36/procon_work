class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letterMap={}
        for i in range(len(s)):
            if s[i] not in letterMap:
                if t[i] in letterMap.values():
                    return False
                letterMap[s[i]] = t[i]
            elif letterMap[s[i]] != t[i]:
                return False
        return True
        