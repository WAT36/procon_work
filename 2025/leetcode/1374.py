class Solution:
    def generateTheString(self, n: int) -> str:
        ans=""
        alphabet="abcdefghijklmnopqrstuvwxyz"
        i=0
        while True:
            if n%2==1:
                ans=ans+(alphabet[i]*n)
                break
            else:
                ans=alphabet[i]
                n-=1
            i+=1
        return ans
            