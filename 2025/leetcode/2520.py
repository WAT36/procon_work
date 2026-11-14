class Solution:
    def countDigits(self, num: int) -> int:
        strnum=str(num)
        ans=0
        for i in range(len(strnum)):
            numi=int(strnum[i])
            if num%numi==0:
                ans+=1
        return ans