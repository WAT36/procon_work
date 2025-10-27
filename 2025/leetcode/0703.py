import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=sorted(nums)

    def add(self, val: int) -> int:
        n=self.nums
        bisect.insort_left(n,val)
        self.nums=n
        #print(n,self.nums,self.k,sorted(n),sorted(n)[::-1][self.k - 1])
        return n[-1*self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)