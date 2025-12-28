class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        while i<len(arr):
            if arr[i]!=0:
                i+=1
            else:
                arr.insert(i,0)
                i+=2
                arr.pop()