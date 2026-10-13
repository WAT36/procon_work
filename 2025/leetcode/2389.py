class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        ans=[0 for _ in range(len(queries))]
        nums.sort()
        ansi=0
        for i in range(len(nums)):
            ansi+=nums[i]
            for j in range(len(queries)):
                if ansi<=queries[j]:
                    ans[j]=max(ans[j],i+1)
            #print(i,ansi,ans)
        return ans