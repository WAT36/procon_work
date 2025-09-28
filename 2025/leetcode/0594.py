class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numset=sorted(list(set(nums)))
        pair=[]
        ans=0
        for i in range(len(numset)-1):
            if numset[i+1]-numset[i]==1:
                pair.append([numset[i],numset[i+1]])

        for p in pair:
            pi_first=nums.index(p[0])
            pj_first=nums.index(p[1])
            pi_last=len(nums)-1-nums[::-1].index(p[0])
            pj_last=len(nums)-1-nums[::-1].index(p[1])
            k_first=min(pi_first,pj_first)
            k_last=max(pi_last,pj_last)
            ans=max(ans,len(list(filter(lambda x: x in p,[nums[k] for k in range(k_first,k_last+1)]))))
            print(p,pi_first,pi_last,pj_first,pj_last,ans)
        return ans
