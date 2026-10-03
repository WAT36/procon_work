class Solution:
    def fillCups(self, amount: list[int]) -> int:
        count=0
        while max(amount)>0:
            amount.sort()
            if amount[-1]>0:
                amount[-1]-=1
            if amount[-2]>0:
                amount[-2]-=1
            count+=1
            #print(amount)
        return count