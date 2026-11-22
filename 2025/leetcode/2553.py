class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans=[]
        for n in nums:
            strn=str(n)
            for i in range(len(strn)):
                ans.append(int(strn[i]))
        return ans