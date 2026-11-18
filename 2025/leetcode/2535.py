class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        es=0
        ds=0
        for n in nums:
            es+=n
            strn=str(n)
            for si in strn:
                ds+=int(si)
        return abs(es-ds)