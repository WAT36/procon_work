class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numset=set(nums)
        list_numset=list(numset)
        for i in range(len(list_numset)):
            if(nums.count(list_numset[i]) >= -(-len(nums)//2)):
                return list_numset[i]