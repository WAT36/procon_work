# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        ans=n
        most=n
        least=0
        while guess(ans) != 0:
            #print(ans,guess(ans))
            if guess(ans) == 1:
                if least < ans:
                    least=ans
                ans = (ans+most)//2
            else:
                if ans < most:
                    most=ans
                ans=(ans+least)//2
        return ans