class Solution:
    def climbStairs(self, n: int) -> int:
        ones=n
        twos=0
        ans=0
        while ones>=0:
            ans+=int(math.factorial(ones+twos)/(math.factorial(ones)*math.factorial(twos)))
            ones-=2
            twos+=1
        return ans