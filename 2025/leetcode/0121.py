class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        while len(prices)>1:
            min_price=min(prices)
            ind=prices.index(min_price)
            ans=max(ans,max([0,*prices[ind+1:]])-min_price)
            prices=prices[:ind]
        return ans

