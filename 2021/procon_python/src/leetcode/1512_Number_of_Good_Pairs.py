import collections

class Solution:
    def comb(self,N,x):
        mod = 10**9+7
        numerator = 1
        for i in range(N-x+1,N+1):
            numerator = numerator *i%mod
        denominator = 1
        for j in range(1,x+1):
            denominator = denominator *j%mod
        d = pow(denominator,mod-2,mod)
        return (numerator*d)%mod

    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=collections.Counter(nums)
        ans=0
        for k,v in l.items():
            if(v==1):
                continue
            else:
                ans+=self.comb(v,2)
        return ans