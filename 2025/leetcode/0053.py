class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm: O(n) time, O(1) space
        現在までの連続和の最大値を一度の走査で更新していく。
        """
        best = curr = nums[0]
        for x in nums[1:]:
            curr = max(x, curr + x)  # ここで「この位置で新しく始めるか/続けるか」を選ぶ
            if curr > best:
                best = curr
        return best