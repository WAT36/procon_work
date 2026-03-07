class Solution:
    def average(self, salary: List[int]) -> float:
        s=sorted(salary)[1:-1]
        return sum(s)/len(s)