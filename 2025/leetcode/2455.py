class Solution:
    def averageValue(self, nums: list[int]) -> int:
        n=list(filter(lambda x: x%3==0 and x%2==0,nums))
        print(n)
        if len(n)==0:
            return 0
        return int(sum(n)/len(list(n)))