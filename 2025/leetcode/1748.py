class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans=[]
        for n in nums:
            if nums.count(n)==1:
                ans.append(n)
        return sum(ans)