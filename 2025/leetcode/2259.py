class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans=""
        for i in range(len(number)):
            #print(i,number[i],ans,number[:i]+number[i+1:])
            if digit == number[i] and ans < number[:i]+number[i+1:]:
                ans=number[:i]+number[i+1:]
        return ans

