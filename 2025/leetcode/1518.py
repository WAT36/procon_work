class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=0
        emptyBottles=0
        while numBottles > 0:
            ans+=numBottles
            ni=numBottles
            ei=emptyBottles
            numBottles=((ni+ei)//numExchange)
            emptyBottles=((ni+ei)%numExchange)
            print(ans,numBottles,emptyBottles)
        ans+=numBottles
        return ans