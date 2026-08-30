class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        m={}
        for i in range(len(nums)-1):
            if nums[i]==key:
                if nums[i+1] in m.keys():
                    m[nums[i+1]]=m[nums[i+1]]+1
                else:
                    m[nums[i+1]]=1
        ans=[-1,-1]
        for k,v in m.items():
            if v > ans[1]:
                ans=[k,v]
        return ans[0]

