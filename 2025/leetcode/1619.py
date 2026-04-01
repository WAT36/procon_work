class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        removes=len(arr)*5//100
        arr=arr[removes:(-1*removes)]
        return sum(arr)/len(arr)