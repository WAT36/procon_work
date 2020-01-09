class Solution:
    def sortArrayByParityII(self, A: list[int]) -> list[int]:
        even=[ai for ai in A if ai%2==0]
        odd=[ai for ai in A if ai%2!=0]
        ans=[]
        for i in range(len(even)):
            ans.append(even[i])
            ans.append(odd[i])
        return ans
