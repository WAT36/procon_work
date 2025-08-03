class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        for i in range(len(candidates)):
            if target - candidates[i] < 0:
                continue
            elif target - candidates[i] == 0:
                ans.append([candidates[i]])
            else:
                ans_i=self.combinationSum(candidates=candidates,target=target-candidates[i])
                ans_i=list(filter(lambda x: x != [],ans_i))
                for j in range(len(ans_i)):    
                    ans.append([candidates[i],*ans_i[j]])
        #print(target,ans)

        finalAns=[]
        sortedAns=[]
        for i in range(len(ans)):
            #print(sorted(ans[i]),finalAns)
            if sorted(ans[i]) not in sortedAns:
                finalAns.append(ans[i])
                sortedAns.append(sorted(ans[i]))
        #print(finalAns)
        return finalAns