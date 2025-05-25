class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth=[sum(i) for i in accounts]
        return max(wealth)