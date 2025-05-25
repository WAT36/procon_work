class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=0
        for i in range(len(arr)):
            j=i+1
            while(j<=len(arr)):
                ans+=sum(arr[i:j])
                j+=2
        return ans
