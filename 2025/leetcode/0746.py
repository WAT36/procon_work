class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costdp=[0 for _ in range(len(cost))]
        costdp[0]=cost[0]
        costdp[1]=cost[1]
        for i in range(2,len(cost)):
            costdp[i]=min(costdp[i-2]+cost[i],costdp[i-1]+cost[i])
        return min(costdp[-1],costdp[-2])
