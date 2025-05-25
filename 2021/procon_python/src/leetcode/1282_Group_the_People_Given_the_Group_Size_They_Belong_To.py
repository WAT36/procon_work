class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        ans=[]
        max_group=max(groupSizes)
        group=[[] for _ in range(max_group+1)]
        for i in range(len(groupSizes)):
            gi=groupSizes[i]
            if(len(group[gi])==gi):
                ans.append(group[gi])
                group[gi]=[]
            group[gi].append(i)

        for i in range(len(group)):
            if(len(group[i]) != 0):
                ans.append(group[i])

        return ans