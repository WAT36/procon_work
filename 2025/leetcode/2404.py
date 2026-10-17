class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        sn=sorted(list(set(nums)))
        maxc=0
        ans=-1
        for sni in sn:
            if sni%2==0 and maxc<nums.count(sni):
                maxc=nums.count(sni)
                ans=sni
        return ans