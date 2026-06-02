class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        for i in range(1,2**len(nums)):
            n=bin(i)[2:].zfill(len(nums))
            ni=[]
            for j in range(len(nums)):
                if n[j]=="1":
                    ni.append(nums[j])
            #print(ni)
            ansi=0
            for nk in ni:
                ansi=ansi^nk
            ans+=ansi
        return ans
