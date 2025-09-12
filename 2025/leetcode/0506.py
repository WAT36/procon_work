class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ss=sorted(score)[::-1]
        ans=[]
        for i in score:
            rank=ss.index(i)+1
            if rank == 1:
                rank="Gold Medal"
            elif rank == 2:
                rank="Silver Medal"
            elif rank == 3:
                rank="Bronze Medal"
            ans.append(str(rank))
        return ans