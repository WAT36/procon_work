class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_arr=list(set(arr))
        count=[]
        for i in range(len(unique_arr)):
            count.append(arr.count(unique_arr[i]))
        count=list(set(count))
        if(len(unique_arr) == len(count)):
            return True
        else:
            return False