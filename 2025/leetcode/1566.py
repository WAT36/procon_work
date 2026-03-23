class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        i=0
        while i+m<=len(arr):
            count=0
            j=i
            while j+m<=len(arr):
                if arr[i:i+m] == arr[j:j+m]:
                    count+=1
                    if count>=k:
                        return True
                else:
                    count=0
                j+=m
            i+=1
        return False