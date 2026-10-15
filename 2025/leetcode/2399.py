class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        alpha="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    if distance[alpha.index(s[i])] != j-i-1:
                        return False
        return True