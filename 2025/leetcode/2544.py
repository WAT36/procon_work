class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans=0
        strn=str(n)
        for i in range(len(strn)):
            ans+=(-1)**(i+2) * int(strn[i])
        return ans