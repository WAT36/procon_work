class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even=[num for num in nums if len(str(num))%2 == 0]
        return len(even)