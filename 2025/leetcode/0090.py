class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        bits=2**len(nums)
        ans=[]
        for i in range(bits):
            bit=bin(i)[2:].zfill(len(nums))
            ansi=[]
            for j in range(len(bit)):
                if bit[j] == '1':
                    ansi.append(nums[j])
            ansi.sort()
            if ansi not in ans:
                ans.append(ansi)
        ans.sort()
        return ans
