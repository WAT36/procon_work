class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        upflag=True
        if arr.index(max(arr)) == 0 or arr.index(max(arr)) == len(arr)-1:
            return False
            
        for i in range(len(arr)-1):
            if upflag:
                if arr[i] < arr[i+1]:
                    pass
                elif arr[i] == arr[i+1]:
                    return False
                else:
                    upflag=False
            else:
                if arr[i] > arr[i+1]:
                    pass
                else:
                    return False
        return True
            