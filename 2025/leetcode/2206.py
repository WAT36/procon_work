class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ns=list(set(nums))
        for n in ns:
            if nums.count(n) % 2 != 0:
                return False
        return True