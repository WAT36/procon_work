class Solution:
    def sortArrayByParity(self, A: list[int]) -> list[int]:
        even=[]
        odd=[]
        for i in range(len(A)):
            if(A[i]%2==0):
                even.append(A[i])
            else:
                odd.append(A[i])
        ans=even
        ans.extend(odd)
        return ans