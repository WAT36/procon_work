class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        mindiff=999999999999999
        ans=[]
        for i in range(len(arr)-1):
            if(abs(arr[i]-arr[i+1]) == mindiff):
                mindiff = abs(arr[i]-arr[i+1])
                ans.append([arr[i],arr[i+1]])
            elif(abs(arr[i]-arr[i+1]) < mindiff):
                mindiff = abs(arr[i]-arr[i+1])
                ans=[[arr[i],arr[i+1]]]
        return ans
