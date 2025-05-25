class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans=0
        for i in range(len(J)):
            ans+=S.count(J[i])
        return ans