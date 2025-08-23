class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length=len(nums)
        bits=(2**length)
        ans=[]
        for i in range(bits):
            bit=bin(i)[2:].zfill(length)
            ans_i=[]
            for j in range(len(nums)):
                if bit[j] == '1':
                    ans_i.append(nums[j])
            ans.append(ans_i)
        return ans
