class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        expectedNums=[]
        for i in range(len(nums)):
            if(nums[i] != val):
                expectedNums.append(nums[i])

        for i in range(len(expectedNums)):
            nums[i] = expectedNums[i]
        return len(expectedNums)
        