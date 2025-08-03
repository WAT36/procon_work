class Solution:
    def addDigits(self, num: int) -> int:
        strnum=str(num)
        ans=num
        while len(strnum) > 1:
            ans=0
            for i in range(len(strnum)):
                ans+=int(strnum[i])
            strnum=str(ans)
        return ans