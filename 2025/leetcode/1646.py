class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums=[]
        for i in range(n+1):
            if i==0:
                nums.append(0)
            elif i==1:
                nums.append(1)
            elif i%2==0:
                nums.append(nums[i//2])
            else:
                x=i//2
                nums.append(nums[x] + nums[x+1])
        return max(nums) 