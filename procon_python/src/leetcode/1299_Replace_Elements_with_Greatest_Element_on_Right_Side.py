class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        rev_arr=list(reversed(arr))
        ans=[-1]
        maxv=-1
        for i in range(len(rev_arr)-1):
            if(maxv < rev_arr[i]):
                maxv=rev_arr[i]
            ans.append(maxv)
        ans=list(reversed(ans))
        return ans
