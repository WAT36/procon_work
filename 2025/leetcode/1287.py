class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr.sort()
        siki=len(arr)/4
        count=0
        maxcount=0
        ans=-1
        for i in range(len(arr)):
            count+=1
            if i < len(arr)-1 and arr[i] != arr[i+1]:
                if count >= maxcount:
                    maxcount=count
                    ans=arr[i]
                count=0
            #print(i,arr[i],count,maxcount,ans)
        else:
            if count >= maxcount:
                maxcount=count
                ans=arr[i]
        return ans