class Solution:
    def reformat(self, s: str) -> str:
        nums=""
        alphas=""
        for si in s:
            if si in "0123456789":
                nums=nums+si
            elif si in "abcdefghijklmnopqrstuvwxyz":
                alphas=alphas+si
        ans=""
        if abs(len(nums)-len(alphas))>1:
            return ans
        elif len(nums)>len(alphas):
            for i in range(len(alphas)):
                ans=ans+nums[i]+alphas[i]
            ans=ans+nums[-1]
            return ans
        else:
            for i in range(len(nums)):
                ans=ans+alphas[i]+nums[i]
            if len(alphas)>len(nums):
                ans=ans+alphas[-1]
            return ans
