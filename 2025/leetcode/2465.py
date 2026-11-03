class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        ansi=[]
        while len(nums)>0:
            mini=min(nums)
            maxi=max(nums)
            nums.remove(mini)
            nums.remove(maxi)
            ansi.append((mini+maxi)/2)
        return len(list(set(ansi)))