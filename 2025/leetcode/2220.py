class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startbin=bin(start)[2:]
        goalbin=bin(goal)[2:]
        l=max(len(startbin),len(goalbin))
        startbin=startbin.zfill(l)
        goalbin=goalbin.zfill(l)
        ans=0
        for i in range(l):
            if startbin[i]!=goalbin[i]:
                ans+=1
        return ans