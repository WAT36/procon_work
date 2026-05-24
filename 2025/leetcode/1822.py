class Solution:
    def arraySign(self, nums: List[int]) -> int:
        minus=0
        for n in nums:
            if n<0:
                minus+=1
            elif n==0:
                return 0
        return  1 if minus%2==0 else -1