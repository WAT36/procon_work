import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            v=heapq.heappop(nums)
            v*=-1
            heapq.heappush(nums,v)
        return sum(nums)