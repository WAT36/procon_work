class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans=0
        prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
        for i in range(left,right+1):
            if bin(i)[2:].count('1') in prime:
                #print(i,bin(i)[2:])
                ans+=1
        return ans