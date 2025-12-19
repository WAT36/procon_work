import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-1*stones[i] for i in range(len(stones))]
        heapq.heapify(stones)
        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            if x==y:
                pass
            else:
                z=x-y
                heapq.heappush(stones,z)
        return -1*heapq.heappop(stones) if len(stones)==1 else 0
