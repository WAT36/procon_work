class Solution:
    def binaryGap(self, n: int) -> int:
        ans=0
        prevind=-1
        binn=bin(n)[2:]
        for i in range(len(binn)):
            if binn[i] == '1':
                if prevind == -1:
                    prevind=i
                else:
                    ans=max(ans,abs(i-prevind))
                    prevind=i
        return ans