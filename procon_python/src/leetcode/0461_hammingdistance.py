class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bin_x=bin(x)[2:].zfill(32)
        bin_y=bin(y)[2:].zfill(32)
        ans=0
        print(bin_x)
        print(bin_y)
        for i in range(len(bin_x)):
            if(bin_x[i] != bin_y[i]):
                ans+=1
        return ans
